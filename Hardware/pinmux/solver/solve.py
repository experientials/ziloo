#!/usr/bin/env python3
"""CP-SAT validator + scorer for the pin-allocation model (board.yaml).

Does the three things the `pin-allocation-eval` method needs automated:
  1. VALIDATE  — is a configuration feasible? (one function per pad; report exact conflicts)
  2. EVALUATE  — score each config on the objective vector; compute the Pareto front
  3. TRACK     — write the objective ledger (ledger.json) + an auto challenge report

Set-packing model: pick one implementation (pad-group) per required feature; no pad used twice.
Run: `python solve.py`  (needs ortools + pyyaml — see requirements.txt).
"""
import json
import pathlib

import yaml
from ortools.sat.python import cp_model

HERE = pathlib.Path(__file__).parent
M = yaml.safe_load((HERE / "board.yaml").read_text())
PADS, FEATS, BASE = M["pads"], M["features"], M.get("baseline", {})
TARGET_LEVEL = 1.8
DIRS = {"pins": "min", "locality": "min", "lanes": "max", "risk": "min", "shifters": "min"}


def opt(feat, oid):
    return next((o for o in FEATS[feat]["options"] if o["id"] == oid), None)


def build_model():
    model = cp_model.CpModel()
    x = {(f, o["id"]): model.NewBoolVar(f"{f}__{o['id']}")
         for f, fd in FEATS.items() for o in fd["options"]}
    for f, fd in FEATS.items():
        s = sum(x[(f, o["id"])] for o in fd["options"])
        model.Add(s == 1) if fd.get("required", True) else model.Add(s <= 1)
    pad_users = {p: [] for p in PADS}
    for f, fd in FEATS.items():
        for o in fd["options"]:
            for p in o["pads"]:
                pad_users[p].append(x[(f, o["id"])])
    for lst in pad_users.values():
        if len(lst) > 1:
            model.Add(sum(lst) <= 1)
    return model, x


def score(sel):
    pins, audioconns, lanes, risk, shifters = set(), set(), 0, 0, 0
    for f, oid in sel.items():
        if oid is None:
            continue
        o = opt(f, oid)
        for p in o["pads"]:
            pins.add(p)
            if FEATS[f].get("audio"):
                audioconns.add(PADS[p]["conn"])
            if PADS[p]["level"] != TARGET_LEVEL:
                shifters += 1
        if f == "audio_speaker":
            lanes = o.get("lanes", 0)
        if not o.get("verified", True):
            risk += 1
    iso = int(sel.get("mcu_control", "").split("_")[0] != sel.get("sensor_bus", "").split("_")[0])
    return {"pins": len(pins), "locality": len(audioconns), "lanes": lanes,
            "risk": risk, "shifters": shifters, "isolation": iso, "sd1": int(bool(sel.get("sd1")))}


def dominates(a, b):
    ge, gt = True, False
    for k, d in DIRS.items():
        av, bv = (a[k], b[k]) if d == "min" else (-a[k], -b[k])
        if av > bv:
            return False
        if av < bv:
            gt = True
    return gt


def validate(sel):
    """Pure conflict report for a (fully/partly) specified selection."""
    users = {}
    for f, oid in sel.items():
        if oid is None:
            continue
        for p in opt(f, oid)["pads"]:
            users.setdefault(p, []).append(f"{f}:{oid}")
    conflicts = {p: u for p, u in users.items() if len(u) > 1}
    return (not conflicts), conflicts


def enumerate_feasible():
    model, x = build_model()

    class C(cp_model.CpSolverSolutionCallback):
        def __init__(self):
            super().__init__()
            self.sols = []

        def on_solution_callback(self):
            self.sols.append({f: oid for (f, oid) in
                              (k for k, v in x.items() if self.Value(v))})
    solver = cp_model.CpSolver()
    solver.parameters.enumerate_all_solutions = True
    c = C()
    solver.Solve(model, c)
    return c.sols


def fmt(sc):
    return " ".join(f"{k}={sc[k]}" for k in ["pins", "locality", "lanes", "risk", "isolation", "sd1"])


def main():
    print("=" * 78)
    print("CP-SAT pin-allocation validator —", M["target"])
    print("=" * 78)

    # 1. VALIDATE the baseline (current plan)
    ok, conf = validate(BASE)
    print(f"\n[1] baseline (current plan): {'FEASIBLE ✓' if ok else 'INFEASIBLE ✗'}")
    print(f"    {fmt(score(BASE))}")
    for p, u in conf.items():
        print(f"    conflict: pad {p} <- {', '.join(u)}")

    # 2. Targeted check: does SD1 + I2C4-on-P20 conflict? (challenge C4)
    probe = dict(BASE, mcu_control="i2c4_p20")
    ok2, conf2 = validate(probe)
    print(f"\n[2] probe: SD1=on AND mcu_control=i2c4_p20 -> {'feasible' if ok2 else 'INFEASIBLE ✗'}")
    for p, u in conf2.items():
        print(f"    conflict: pad {p} <- {', '.join(u)}")

    # 3. EVALUATE — enumerate all feasible configs, compute Pareto front
    sols = enumerate_feasible()
    scored = [(s, score(s)) for s in sols]
    front = [(s, sc) for s, sc in scored
             if not any(dominates(o, sc) for o2, o in scored if o is not sc)]
    print(f"\n[3] feasible configs: {len(scored)}   Pareto-optimal: {len(front)}")
    print("    Pareto front (non-dominated):")
    for s, sc in sorted(front, key=lambda t: (t[1]["risk"], -t[1]["lanes"])):
        tag = "  <- baseline" if s == BASE else ""
        spk, mic = s.get("audio_speaker"), s.get("audio_mic")
        print(f"      spk={spk:<5} mic={mic:<5} sd1={s.get('sd1','-'):<3} mcu={s.get('mcu_control')}  |  {fmt(sc)}{tag}")

    # 4. TRACK — write ledger
    ledger = [{"config": s, "objectives": sc, "pareto": (s, sc) in front} for s, sc in scored]
    (HERE / "ledger.json").write_text(json.dumps(ledger, indent=2))
    print(f"\n[4] wrote ledger.json ({len(ledger)} configs)")


if __name__ == "__main__":
    main()
