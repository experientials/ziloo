#!/usr/bin/env python3
"""Loader: assemble a PRODUCT from its module/board files into one flat view.

Layout:
  common.yaml         shared tag_vocab + defaults (every product)
  modules/<m>.yaml    a component installed on a host board (the SoM)
  boards/<b>.yaml     a host board: connectors, chips, pins (som+func+dest)  [2-layer: func here]
  products/<p>.yaml   modules + boards it comprises (+ kicad, product connectors)

load_product(name) returns a dict shaped like the old single pins.yaml so the existing
check/render logic consumes it unchanged:
  {meta, tag_vocab, connectors, connector_registry, pins, pin_board, modules, boards, product}
"""
import pathlib

import yaml

HERE = pathlib.Path(__file__).parent


def _load(p):
    return yaml.safe_load(p.read_text())


def list_products():
    return sorted(p.stem for p in (HERE / "products").glob("*.yaml"))


def _need(kind, n, name):
    p = HERE / kind / f"{n}.yaml"
    if not p.exists():
        raise SystemExit(f"loader: product '{name}' references missing "
                         f"{kind[:-1]} '{n}' — no {kind}/{n}.yaml")
    return _load(p)


def load_product(name):
    common = _load(HERE / "common.yaml")
    prod = _load(HERE / "products" / f"{name}.yaml")
    modules = {m: _need("modules", m, name) for m in prod.get("modules", [])}
    boards = {b: _need("boards", b, name) for b in prod.get("boards", [])}

    pins, pin_board, connectors, registry = {}, {}, {}, {}
    for bname, bd in boards.items():
        for k, v in (bd.get("pins") or {}).items():
            if k in pins:
                raise SystemExit(f"loader: duplicate pin key {k} across boards "
                                 f"({pin_board[k]} & {bname}) in product '{name}'")
            pins[k], pin_board[k] = v, bname
        for c, cv in (bd.get("connectors") or {}).items():
            connectors[c] = {**cv, "_board": bname}
        # `board` is DERIVED from the owning file, never hand-authored → can't drift.
        for r, rv in (bd.get("connector_registry") or {}).items():
            registry[r] = {**rv, "board": bname}
    for r, rv in (prod.get("connector_registry") or {}).items():
        registry[r] = {**rv, "board": rv.get("board", "product")}

    meta = {"product": name, "name": prod.get("name"),
            "modules": list(modules), "boards": list(boards),
            "kicad": prod.get("kicad"),
            "default_level": common.get("default_level")}
    return {"meta": meta, "tag_vocab": common.get("tag_vocab", {}),
            "connectors": connectors, "connector_registry": registry,
            "pins": pins, "pin_board": pin_board,
            "modules": modules, "boards": boards, "product": prod}
