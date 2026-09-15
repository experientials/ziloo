#!/usr/bin/env python3
"""Render Markdown views from the canonical pins.yaml (source of truth).

Generates into generated/:
  P20.md, P21.md, P10.md   — by-pin allocation tables
  sound_connector_cable.md — 20-pin DF40 sound connector -> header (from `dest: Sound pN`)
  by_destination.md        — pins grouped by connector/circuit they feed
Do not hand-edit generated/ — edit pins.yaml and re-run (`make render`).
"""
import pathlib
import re

import yaml

HERE = pathlib.Path(__file__).parent
GEN = HERE / "generated"
GEN.mkdir(exist_ok=True)
DOC = yaml.safe_load((HERE / "pins.yaml").read_text())
PINS = DOC["pins"]
BANNER = "<!-- GENERATED from pins.yaml by render.py — do not hand-edit. -->\n"


def num(pin):  # "P20.7" -> 7
    return int(pin.split(".")[1])


def rows(conn):
    return sorted((p for p in PINS if p.startswith(conn + ".")), key=num)


def alts(d):
    return ", ".join(d.get("alts", [])) or ""


def render_header(conn, path):
    lines = [BANNER, f"## {conn} — allocation (by pin)\n",
             "| Pin | SoM | Function | Destination | Alt mux | Verified |",
             "|---|---|---|---|---|---|"]
    for p in rows(conn):
        d = PINS[p]
        v = d.get("verified", "")
        lines.append(f"| {p} | {d.get('som','—')} | {d['func']} | {d.get('dest','')} | {alts(d)} | {v} |")
    path.write_text("\n".join(lines) + "\n")
    return len(rows(conn))


def render_p10(path):
    lines = [BANNER, "## P10 — power / reset / system-control (2×5, DR10SM)\n",
             "⚠ pin order tentative — verify against carrier schematic sheet 6.\n",
             "| Pin | Signal | SoM | Note |", "|---|---|---|---|"]
    for p in rows("P10"):
        d = PINS[p]
        lines.append(f"| {p} | {d['func']} | {d.get('som','—')} | {d.get('dest','')} |")
    path.write_text("\n".join(lines) + "\n")


def render_sound_cable(path):
    # pins whose dest contains "Sound pN" -> DF40 pin N
    rx = re.compile(r"Sound p(\d+)")
    rowset = []
    for p, d in PINS.items():
        m = rx.search(d.get("dest", ""))
        if m:
            rowset.append((int(m.group(1)), d["func"], p, d.get("som", "—")))
    rowset.sort()
    lines = [BANNER, "## Sound connector (20-pin DF40) → carrier header\n",
             "Generated from `dest: Sound pN`. Power/GND pins (DF40 1/9/10/20) identify on the board.\n",
             "| DF40 pin | Signal | → Header | SoM |", "|---|---|---|---|"]
    for n, func, hdr, som in rowset:
        lines.append(f"| {n} | {func} | **{hdr}** | {som} |")
    path.write_text("\n".join(lines) + "\n")
    return len(rowset)


def render_by_dest(path):
    groups = {}
    for p, d in PINS.items():
        key = re.sub(r"\s*p\d+.*$", "", d.get("dest", "?")).strip() or "?"
        groups.setdefault(key, []).append(p)
    lines = [BANNER, "## Pins by destination / circuit\n"]
    for key in sorted(groups):
        pset = sorted(groups[key], key=lambda p: (p.split(".")[0], num(p)))
        lines.append(f"- **{key}** ({len(pset)}): {', '.join(pset)}")
    path.write_text("\n".join(lines) + "\n")
    return len(groups)


def render_connectors(path):
    reg = DOC.get("connector_registry", {})
    order = {"placed": 0, "given": 1, "draft": 2}
    items = sorted(reg.items(),
                   key=lambda kv: (order.get(kv[1].get("status"), 9), kv[0]))
    lines = [BANNER, "## Connector registry\n",
             "First-class connectors beyond the P20/P21/P10 headers. "
             "`given` = vendor-fixed · `placed` = drawn in KiCad · `draft` = planned.\n",
             "| Connector | Board | Type | Pos | Status | Part | Pinout | How it connects |",
             "|---|---|---|---|---|---|---|---|"]
    for cid, e in items:
        key = f"Key {e['keying']}" + ("?" if e.get("keying_status") == "TBD" else "")
        doc = e.get("pinout", "")
        doclink = f"[doc]({doc})" if doc else "—"
        lines.append(
            f"| **{e.get('name', cid)}** | {e.get('board','—')} | {e.get('role','')} {key} "
            f"| {e.get('positions','—')} | {e['status']} | {e.get('part','—')} | {doclink} "
            f"| {e.get('connects', e.get('purpose',''))} |")
    for cid, e in items:
        if e.get("note") or e.get("alternatives"):
            lines.append(f"\n**{e.get('name', cid)}** — {e.get('note','')}"
                         + (f" _Alt:_ {e['alternatives']}" if e.get("alternatives") else ""))
    path.write_text("\n".join(lines) + "\n")
    return len(reg)


def render_by_tag(path):
    tags = {}
    for p, d in PINS.items():
        for t in d.get("tags", []):
            tags.setdefault(t, []).append(p)
    lines = [BANNER, "## Pins by tag\n"]
    for t in sorted(tags):
        pset = sorted(tags[t], key=lambda p: (p.split(".")[0], num(p)))
        lines.append(f"- **{t}** ({len(pset)}): {', '.join(pset)}")
    path.write_text("\n".join(lines) + "\n")
    return len(tags)


def main():
    n20 = render_header("P20", GEN / "P20.md")
    n21 = render_header("P21", GEN / "P21.md")
    render_p10(GEN / "P10.md")
    ns = render_sound_cable(GEN / "sound_connector_cable.md")
    nd = render_by_dest(GEN / "by_destination.md")
    nt = render_by_tag(GEN / "by_tag.md")
    nc = render_connectors(GEN / "connectors.md")
    print(f"rendered: P20 ({n20}) P21 ({n21}) P10 ({len(rows('P10'))}) "
          f"sound-cable ({ns} signals) destinations ({nd}) tags ({nt}) "
          f"connectors ({nc}) -> {GEN}/")


if __name__ == "__main__":
    main()
