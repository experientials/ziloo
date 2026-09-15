#!/usr/bin/env python3
"""Cross-check the pin-allocation YAMLs for consistency across connectors and chips.

Hard errors (exit 1):
  E1  a SoM ball (P1.x/P2.x) allocated to more than one header pin
  E2  a header pin number out of its connector's range, or an unknown connector
  E3  cross-file drift: a pad's connector in solver/board.yaml disagrees with pins.yaml
  E4  the 20-pin DF40 sound connector is incomplete/duplicated (signal pins 2-8,11-19)
Warnings (exit 0):
  W1  a signal/function that lands on more than one connector (intended multi-drop? confirm)
  W2  a solver pad not grounded in pins.yaml (possible model drift)
  K*  KiCad ground-truth drift (model vs the drawn schematic) — see kicad_checks()
Run: `make check`.
"""
import glob
import pathlib
import re
import sys

import yaml

HERE = pathlib.Path(__file__).parent
PINS = yaml.safe_load((HERE / "pins.yaml").read_text())
BOARD = yaml.safe_load((HERE / "solver" / "board.yaml").read_text())
P = PINS["pins"]
CONN_MAX = {"P20": 34, "P21": 34, "P10": 10}

errors, warns = [], []


def conn_of(pin):
    return pin.split(".")[0]


# E1 — SoM ball uniqueness
som_users = {}
for pin, d in P.items():
    som = d.get("som")
    if som:
        som_users.setdefault(som, []).append(pin)
for som, users in sorted(som_users.items()):
    if len(users) > 1:
        errors.append(f"E1 SoM ball {som} allocated to {len(users)} header pins: {', '.join(users)}")

# E2 — pin range / known connector
for pin in P:
    c = conn_of(pin)
    if c not in CONN_MAX:
        errors.append(f"E2 {pin}: unknown connector {c}")
        continue
    n = int(pin.split(".")[1])
    if not (1 <= n <= CONN_MAX[c]):
        errors.append(f"E2 {pin}: pin {n} out of range 1..{CONN_MAX[c]} for {c}")

# E3 — cross-file pad↔connector consistency (pins.yaml pad: vs solver board.yaml pads:)
board_pads = BOARD.get("pads", {})
pad_conn_pins = {}  # pad -> connector (from pins.yaml `pad:` field)
for pin, d in P.items():
    pad = d.get("pad")
    if pad:
        pad_conn_pins.setdefault(pad, set()).add(conn_of(pin))
for pad, meta in board_pads.items():
    if pad in pad_conn_pins:
        cset = pad_conn_pins[pad]
        if meta["conn"] not in cset:
            errors.append(f"E3 pad {pad}: board.yaml conn={meta['conn']} but pins.yaml has {sorted(cset)}")

# W2 — solver pads grounded in pins.yaml? (only checks named silicon pads, not the I2C aux pads)
grounded = set(pad_conn_pins) | {"SAI3_MCLK", "SAI3_RXD", "SAI3_RXC", "SAI3_RXFS",
                                 "SAI3_TXD", "SAI3_TXC", "SAI3_TXFS"}
for feat, fd in BOARD["features"].items():
    for o in fd["options"]:
        for pad in o["pads"]:
            if pad.startswith(("ENET_", "SAI3_", "GPIO4")) and pad not in board_pads:
                warns.append(f"W2 solver feature {feat}:{o['id']} uses pad {pad} not declared in board.yaml pads")

# E4 — sound DF40 completeness (signal pins 2-8, 11-19; power at 1,9,10,20)
rx = re.compile(r"Sound p(\d+)")
df40 = {}
for pin, d in P.items():
    m = rx.search(d.get("dest", ""))
    if m:
        df40.setdefault(int(m.group(1)), []).append(pin)
expected = set(range(2, 9)) | set(range(11, 20))  # 2-8, 11-19
got = set(df40)
for n in sorted(df40):
    if len(df40[n]) > 1:
        errors.append(f"E4 DF40 pin {n} claimed by {', '.join(df40[n])}")
missing = expected - got
extra = got - expected
if missing:
    errors.append(f"E4 sound connector missing DF40 signal pins: {sorted(missing)}")
if extra:
    errors.append(f"E4 sound connector has unexpected DF40 pins (power slots?): {sorted(extra)}")

# E5 — tags must be in the controlled vocabulary
vocab = set()
for facet in PINS.get("tag_vocab", {}).values():
    vocab.update(facet)
for pin, d in P.items():
    for t in d.get("tags", []):
        if t not in vocab:
            errors.append(f"E5 {pin}: tag '{t}' not in tag_vocab")

# W1 — a function on more than one connector
func_conns = {}
for pin, d in P.items():
    func_conns.setdefault(d["func"], set()).add(conn_of(pin))
for func, cs in sorted(func_conns.items()):
    if len(cs) > 1:
        warns.append(f"W1 function {func} lands on connectors {sorted(cs)} (intended multi-drop?)")

# K* — KiCad ground-truth: does the drawn schematic match the model?
# Drift is legitimate during design (board may lead/lag the plan) → warnings, never errors.
def kicad_checks():
    cfg = PINS["meta"].get("kicad")
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

    labels_by_sheet = {}
    placed_ds = set()
    for f in sheets:
        txt = pathlib.Path(f).read_text()
        labels_by_sheet[pathlib.Path(f).name] = set(label_rx.findall(txt))
        placed_ds.update(m + "DS" for m in fp_rx.findall(txt))
    all_labels = set().union(*labels_by_sheet.values()) if labels_by_sheet else set()
    audio_labels = {n for n in all_labels if n.startswith(audio)}

    # K1 — is the audio bus family present on the board at all?
    if not audio_labels:
        warns.append(f"K1 no '{audio}*' net labels found in {schdir.name} — "
                     f"audio bus modelled but not drawn?")

    # K2 — the planned sound connector placement (model vs board)
    want = cfg.get("sound_connector")
    sound_pins = sum(1 for d in P.values()
                     if d.get("dest", "").startswith("Sound p"))
    if want and want not in placed_ds and sound_pins:
        warns.append(f"K2 {sound_pins} pins modelled onto a {want} DF40 sound "
                     f"connector, but no {want} footprint is placed in "
                     f"{schdir.name} (placed: {sorted(placed_ds)}) — audio rides "
                     f"another connector (planned≠built).")

    # K3 — C5 automation: audio bus level-shifted into a 3V3 net (product = 1V8)
    shifted = sorted(s for s, labs in labels_by_sheet.items()
                     if any(n.startswith(audio) for n in labs)
                     and net3v3_rx.search(pathlib.Path(schdir / s).read_text()))
    if shifted:
        warns.append(f"K3 audio bus ({audio}*) shares a sheet with a 3V3 net in "
                     f"{shifted} — level-shift off 1V8 (challenge C5).")

    print(f"note: K-checks vs {schdir.name} — {len(sheets)} sheets, "
          f"{len(audio_labels)} {audio}* nets, DF40 placed: {sorted(placed_ds)}")


def registry_checks():
    # K4 — audit the connector_registry: linked docs exist; `placed` connectors are
    # actually drawn (sheet exists + part appears). Drift → warning, never error.
    reg = PINS.get("connector_registry", {})
    if not reg:
        return
    hw = (HERE / "..").resolve()  # ziloo/Hardware — kicad: paths are relative to here
    counts = {}
    for cid, e in reg.items():
        counts[e.get("status", "?")] = counts.get(e.get("status", "?"), 0) + 1
        doc = e.get("pinout")
        if doc and not (HERE / doc).exists():
            warns.append(f"K4 {cid}: pinout doc '{doc}' not found")
        if e.get("status") == "placed":
            sh = e.get("kicad")
            if not sh:
                warns.append(f"K4 {cid}: status=placed but no `kicad:` sheet given")
            elif not (hw / sh).exists():
                warns.append(f"K4 {cid}: placed sheet '{sh}' not found")
            else:
                part = e.get("part", "")
                pn = re.search(r"[0-9]{6,}[-A-Z0-9]*", part or "")
                if pn and pn.group(0) not in (hw / sh).read_text():
                    warns.append(f"K4 {cid}: part '{pn.group(0)}' not found in {sh} "
                                 f"(placed but drift?)")
    summary = ", ".join(f"{k}:{v}" for k, v in sorted(counts.items()))
    print(f"note: connector_registry — {len(reg)} connectors ({summary})")


kicad_checks()
registry_checks()

# --- report ---
for w in warns:
    print("warn:", w)
for e in errors:
    print("ERROR:", e)
print(f"\ncheck: {len(errors)} error(s), {len(warns)} warning(s)  "
      f"[{len(P)} pins, {len(som_users)} SoM balls, {len(got)} sound signals]")
sys.exit(1 if errors else 0)
