#!/usr/bin/env python3
"""Cross-check the pin-allocation model for consistency, per PRODUCT.

A product is assembled from module + board files by model.py. Each product is checked
independently. Usage: `make check` (all products) or `python check.py <product>`.

Hard errors (exit 1):
  S   structural: a file violates schemas/pinmux.schema.json (typo'd/unknown field, missing
      required field, bad enum value) — the "extent of information" contract
  E1  a SoM ball (P1.x/P2.x) allocated to more than one pin (within the product)
  E2  a pin number out of its connector's range, or an unknown connector
  E3  cross-file drift: a pad's connector in solver/board.yaml disagrees with the board pins
  E4  the 20-pin DF40 sound connector is incomplete/duplicated (signal pins 2-8,11-19)
  E5  a tag not in the controlled vocabulary
Warnings (exit 0):
  F   connector fullness: a declared position 1..pins is undefined (a "hole"). Acknowledge
      power/GND/NC via `power_pins:`; `complete: true` promotes any remaining hole to an error.
  W1  a function that lands on more than one connector (intended multi-drop? confirm)
  W2  a solver pad not grounded in the board pins (possible model drift)
  K*  KiCad ground-truth drift (model vs the drawn schematic) + connector-registry audit
"""
import glob
import json
import pathlib
import re
import sys
from collections import Counter

import yaml
from jsonschema import Draft7Validator

import model

HERE = pathlib.Path(__file__).parent
BOARD = yaml.safe_load((HERE / "solver" / "board.yaml").read_text())
SCHEMA = json.loads((HERE / "schemas" / "pinmux.schema.json").read_text())


def _validate(obj, defname, label, errors):
    sub = {"$ref": f"#/$defs/{defname}", "$defs": SCHEMA["$defs"]}
    for e in sorted(Draft7Validator(sub).iter_errors(obj),
                    key=lambda e: list(e.path)):
        loc = "/".join(str(x) for x in e.path)
        errors.append(f"S {label}{('.' + loc) if loc else ''}: {e.message}")


MODULES = {p.stem for p in (HERE / "modules").glob("*.yaml")}
BOARDS = {p.stem for p in (HERE / "boards").glob("*.yaml")}


def schema_checks(M, errors):
    # S — structural: every file conforms to schemas/pinmux.schema.json (typos, missing
    # required fields, bad enums). Raw file dicts, not the merged view.
    for m, d in M["modules"].items():
        _validate(d, "module", f"module:{m}", errors)
    for b, d in M["boards"].items():
        _validate(d, "board", f"board:{b}", errors)
    _validate(M["product"], "product", f"product:{M['meta']['product']}", errors)


def naming_checks(M, errors):
    # N — cross-file reference integrity. Ids are FILENAME STEMS; product.modules/boards
    # resolving to files is enforced by the loader. Here: board.hosts -> a real module that
    # the product actually includes. (registry `board` is loader-derived, so it can't drift.)
    prod_mods = set(M["meta"]["modules"])
    for b, bd in M["boards"].items():
        for h in bd.get("hosts", []):
            if h not in MODULES:
                errors.append(f"N board:{b} hosts unknown module '{h}' "
                              f"(no modules/{h}.yaml)")
            elif h not in prod_mods:
                errors.append(f"N board:{b} hosts module '{h}' but product "
                              f"'{M['meta']['product']}' doesn't list it "
                              f"(modules: {sorted(prod_mods)})")

    # N (som) — every pin `som` must land in the module ball space (union across the
    # product's modules). Catches wrong-connector / out-of-range ball refs.
    ballspace = {}
    for md in M["modules"].values():
        for bc, spec in (md.get("balls") or {}).items():
            ballspace[bc] = spec.get("count", 0)
    for pin, d in M["pins"].items():
        som = d.get("som")
        if not som:
            continue
        mm = re.match(r"^(P\d+)\.(\d+)$", som)
        if not mm:
            errors.append(f"N {pin}: som '{som}' malformed (expect P<n>.<m>)")
        elif ballspace and (mm.group(1) not in ballspace
                            or not 1 <= int(mm.group(2)) <= ballspace[mm.group(1)]):
            errors.append(f"N {pin}: som '{som}' outside module ball space "
                          f"{ballspace}")


def fullness_checks(M, warns, errors):
    # F — connector fullness: which of a connector's 1..pins positions are undefined (holes).
    # power/GND/NC positions can be acknowledged via `power_pins:`. `complete: true` promotes
    # any remaining hole to a hard error; otherwise it's a warning to review.
    by_conn = {}
    for p in M["pins"]:
        c, n = p.rsplit(".", 1)
        by_conn.setdefault(c, set()).add(int(n))
    for c, cv in M["connectors"].items():
        n = cv.get("pins")
        defined = by_conn.get(c, set())
        if not n or (not defined and not cv.get("complete")):
            continue  # pure stub (0 pins) is reported by `extent`, not as holes
        holes = sorted(set(range(1, n + 1))
                       - defined - set(cv.get("power_pins", [])))
        if not holes:
            continue
        msg = f"F {c}: undefined position(s) {holes} of {n}"
        if cv.get("complete"):
            errors.append(msg + " (connector marked `complete`)")
        else:
            warns.append(msg + " — power/GND/NC? add `power_pins:` to acknowledge")


def extent(M):
    # Completeness / confidence report — how much do we actually KNOW vs stub/guess.
    pins = M["pins"]
    ver = Counter(d.get("verified", "unverified") for d in pins.values())
    withpins = {p.split(".")[0] for p in pins}
    stubs = sorted(c for c in M["connectors"] if c not in withpins)
    reg = M["connector_registry"]
    rstatus = Counter(e.get("status", "?") for e in reg.values())
    # placed connectors that lack a pinout/pin-map, or any entry with no description at all
    thin = sorted(k for k, e in reg.items()
                  if (e.get("status") == "placed" and not e.get("pinout"))
                  or not (e.get("pinout") or e.get("connects") or e.get("purpose")))
    vshown = ", ".join(f"{k}={v}" for k, v in sorted(ver.items()))
    print(f"extent: pins verified [{vshown}] · connectors {len(withpins)}/"
          f"{len(M['connectors'])} populated"
          + (f", stubs {stubs}" if stubs else "")
          + f" · registry {dict(rstatus)}"
          + (f", thin {thin}" if thin else ""))


def conn_of(pin):
    return pin.split(".")[0]


def check_product(name):
    try:
        M = model.load_product(name)
    except SystemExit as e:  # bad cross-file reference (missing module/board, dup pin)
        print(f"\n=== product '{name}' ===\nERROR: N {e}")
        return 1
    P = M["pins"]
    connectors = M["connectors"]
    conn_max = {c: cv.get("pins") for c, cv in connectors.items()}
    errors, warns = [], []

    # E1 — SoM ball uniqueness. Exception: connectors declared `alt_of` each other are
    # ALTERNATIVE footprints on the same balls (only one is populated per build), so they may
    # legitimately share a ball. A duplicate WITHIN one connector is always an error.
    alt_parent = {c: cv["alt_of"] for c, cv in connectors.items() if cv.get("alt_of")}

    def alt_root(c):
        seen = set()
        while c in alt_parent and c not in seen:
            seen.add(c)
            c = alt_parent[c]
        return c

    som_users = {}
    for pin, d in P.items():
        if d.get("som"):
            som_users.setdefault(d["som"], []).append(pin)
    for som, users in sorted(som_users.items()):
        if len(users) <= 1:
            continue
        conns = [conn_of(u) for u in users]
        same_conn_dup = len(set(conns)) < len(conns)
        if same_conn_dup or len({alt_root(c) for c in conns}) > 1:
            errors.append(f"E1 SoM ball {som} allocated to {len(users)} pins: "
                          f"{', '.join(users)}")

    # E2 — pin range / known connector
    for pin in P:
        c = conn_of(pin)
        if c not in conn_max:
            errors.append(f"E2 {pin}: unknown connector {c}")
            continue
        n = int(pin.split(".")[1])
        hi = conn_max[c]
        if hi and not (1 <= n <= hi):
            errors.append(f"E2 {pin}: pin {n} out of range 1..{hi} for {c}")

    # E3 — cross-file pad<->connector consistency (board pins `pad:` vs solver board.yaml)
    board_pads = BOARD.get("pads", {})
    pad_conns = {}
    for pin, d in P.items():
        if d.get("pad"):
            pad_conns.setdefault(d["pad"], set()).add(conn_of(pin))
    for pad, meta in board_pads.items():
        if pad in pad_conns and meta["conn"] not in pad_conns[pad]:
            errors.append(f"E3 pad {pad}: board.yaml conn={meta['conn']} but pins "
                          f"has {sorted(pad_conns[pad])}")

    # W2 — solver pads grounded in the board pins?
    if pad_conns:  # only meaningful when this product has the pad-bearing (carrier) board
        for feat, fd in BOARD["features"].items():
            for o in fd["options"]:
                for pad in o["pads"]:
                    if pad.startswith(("ENET_", "SAI3_", "GPIO4")) \
                            and pad not in board_pads:
                        warns.append(f"W2 solver {feat}:{o['id']} uses pad {pad} "
                                     f"not declared in board.yaml pads")

    # E4 — sound DF40 completeness (signal pins 2-8, 11-19; power at 1,9,10,20)
    rx = re.compile(r"Sound p(\d+)")
    df40 = {}
    for pin, d in P.items():
        m = rx.search(d.get("dest", ""))
        if m:
            df40.setdefault(int(m.group(1)), []).append(pin)
    if df40:  # only if this product routes a sound connector
        expected = set(range(2, 9)) | set(range(11, 20))
        for n in sorted(df40):
            if len(df40[n]) > 1:
                errors.append(f"E4 DF40 pin {n} claimed by {', '.join(df40[n])}")
        missing, extra = expected - set(df40), set(df40) - expected
        if missing:
            errors.append(f"E4 sound connector missing DF40 pins: {sorted(missing)}")
        if extra:
            errors.append(f"E4 sound connector unexpected DF40 pins: {sorted(extra)}")

    # E5 — tags in the controlled vocabulary
    vocab = set()
    for facet in M["tag_vocab"].values():
        vocab.update(facet)
    for pin, d in P.items():
        for t in d.get("tags", []):
            if t not in vocab:
                errors.append(f"E5 {pin}: tag '{t}' not in tag_vocab")

    # W1 — a function on more than one connector (ground/rails multi-drop by design → skip).
    # Alternative footprints (alt_of) legitimately carry the same function → collapse to alt-root.
    # Power/GND/rail nets (no `som` on any pin) also multi-drop by design → skip.
    W1_SKIP = {"GND"}
    func_conns = {}
    func_has_som = {}
    for pin, d in P.items():
        func_conns.setdefault(d["func"], set()).add(conn_of(pin))
        func_has_som[d["func"]] = func_has_som.get(d["func"], False) or bool(d.get("som"))
    for func, cs in sorted(func_conns.items()):
        if func in W1_SKIP or not func_has_som.get(func):
            continue  # rails/GND legitimately appear on multiple connectors
        if len({alt_root(c) for c in cs}) > 1:
            warns.append(f"W1 function {func} on connectors {sorted(cs)} "
                         f"(intended multi-drop?)")

    schema_checks(M, errors)
    naming_checks(M, errors)
    fullness_checks(M, warns, errors)
    kicad_checks(M, warns)
    registry_checks(M, warns)

    print(f"\n=== product '{name}' ({M['meta']['name']}) — "
          f"boards: {M['meta']['boards']} ===")
    for w in warns:
        print("warn:", w)
    for e in errors:
        print("ERROR:", e)
    extent(M)
    print(f"check: {len(errors)} error(s), {len(warns)} warning(s)  "
          f"[{len(P)} pins, {len(som_users)} SoM balls, {len(df40)} sound signals]")
    return len(errors)


def kicad_checks(M, warns):
    # K1-3 — model vs the drawn KiCad schematic (this product's `kicad:`). Drift → warning.
    cfg = M["meta"].get("kicad")
    if not cfg:
        return
    schdir = (HERE / cfg["schematic_dir"]).resolve()
    sheets = [p for p in glob.glob(str(schdir / "*.kicad_sch"))
              if "_autosave" not in p]
    if not sheets:
        print(f"note: K-checks skipped — no *.kicad_sch under {schdir}")
        return
    label_rx = re.compile(r"\((?:label|global_label|hierarchical_label) \"([^\"]+)\"")
    fp_rx = re.compile(r"property \"Footprint\" \"[^\"]*DF40\w*-(\d+)DS")
    net3v3_rx = re.compile(r"\"(?:\+?3V3)\"|\(name \"3V3\"")
    audio = cfg.get("audio_net_prefix", "SAI5")

    labels_by_sheet, placed_ds = {}, set()
    for f in sheets:
        txt = pathlib.Path(f).read_text()
        labels_by_sheet[pathlib.Path(f).name] = set(label_rx.findall(txt))
        placed_ds.update(m + "DS" for m in fp_rx.findall(txt))
    all_labels = set().union(*labels_by_sheet.values())
    audio_labels = {n for n in all_labels if n.startswith(audio)}

    if not audio_labels:
        warns.append(f"K1 no '{audio}*' net labels in {schdir.name} — "
                     f"audio bus modelled but not drawn?")
    want = cfg.get("sound_connector")
    sound_pins = sum(1 for d in M["pins"].values()
                     if d.get("dest", "").startswith("Sound p"))
    if want and want not in placed_ds and sound_pins:
        warns.append(f"K2 {sound_pins} pins modelled onto a {want} DF40 sound "
                     f"connector, but no {want} footprint is placed in "
                     f"{schdir.name} (placed: {sorted(placed_ds)}) — audio rides "
                     f"another connector (planned≠built).")
    shifted = sorted(s for s, labs in labels_by_sheet.items()
                     if any(n.startswith(audio) for n in labs)
                     and net3v3_rx.search(pathlib.Path(schdir / s).read_text()))
    if shifted:
        warns.append(f"K3 audio bus ({audio}*) shares a sheet with a 3V3 net in "
                     f"{shifted} — level-shift off 1V8 (challenge C5).")
    print(f"note: K-checks vs {schdir.name} — {len(sheets)} sheets, "
          f"{len(audio_labels)} {audio}* nets, DF40 placed: {sorted(placed_ds)}")


def registry_checks(M, warns):
    # K4 — audit connector_registry: linked docs exist; `placed` connectors are drawn.
    reg = M["connector_registry"]
    if not reg:
        return
    hw = (HERE / "..").resolve()  # ziloo/Hardware — kicad: paths relative to here
    counts = {}
    for cid, e in reg.items():
        counts[e.get("status", "?")] = counts.get(e.get("status", "?"), 0) + 1
        doc = e.get("pinout")
        if doc and not (HERE / doc).exists():
            warns.append(f"K4 {cid}: pinout doc '{doc}' not found")
        if e.get("status") == "placed":
            sh = e.get("kicad")
            if not sh:
                warns.append(f"K4 {cid}: status=placed but no `kicad:` sheet")
            elif not (hw / sh).exists():
                warns.append(f"K4 {cid}: placed sheet '{sh}' not found")
            else:
                pn = re.search(r"[0-9]{6,}[-A-Z0-9]*", e.get("part", "") or "")
                if pn and pn.group(0) not in (hw / sh).read_text():
                    warns.append(f"K4 {cid}: part '{pn.group(0)}' not in {sh} (drift?)")
    summary = ", ".join(f"{k}:{v}" for k, v in sorted(counts.items()))
    print(f"note: connector_registry — {len(reg)} connectors ({summary})")


def main():
    products = sys.argv[1:] or model.list_products()
    total = sum(check_product(p) for p in products)
    print(f"\n{'=' * 60}\nTOTAL: {total} error(s) across {len(products)} product(s)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
