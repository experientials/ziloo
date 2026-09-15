# Pin-allocation challenges (adversarial evaluation)

ATAM-style challenges against the current plan — each names the objective stressed, a concrete
dominating candidate, and the tradeoff it costs. Method: the `pin-allocation-eval` skill.
Model in `model.yaml`; formal solver model in `solver/board.yaml`; ledger in `solver/ledger.json`.

## Ground-truth cross-check (KiCad, `check.py` K-series, run 2026-09-15)
`check.py` now compares the **model** against the **drawn** `929/Faceboard` schematic (14 sheets).
Drift is legitimate during design → warnings, not errors. Two fire today:
- **K2 — the 20-pin sound connector is planned, not built.** 16 pins are modelled onto a
  `20DS` DF40, but no `20DS` footprint is placed anywhere (placed: 100/60/50/34DS; `sound.kicad_sch`
  is empty). Audio currently rides the **60-pin DF40** on `media-domain`. The DF40HC(3.5)-20DS is a
  BOM/doc part, not yet on the board — treat the sound-cable rendering as *intent*.
- **K3 — C5 confirmed in silicon.** The `SAI5*` bus shares `media-domain.kicad_sch` with a 3V3 net
  (shifters U19/U20/U21 = 3× TXS0104). This is the 1V8-everywhere violation, now caught automatically.
- **SAI5 vindicated:** the schematic uses `SAI5_*` net names throughout (13 labels) — matches the
  product plan (C2/C3 decision). The audio *bus choice* and the board agree; only the *connector*
  and *voltage domain* drift.

## Automated validation (CP-SAT, `solver/solve.py`, run 2026-09-14)
- **Baseline is FEASIBLE** — the 16 ENET pads fit exactly (pins=32, lanes=4, risk=2, isolation=1).
  → **C1 below is REFUTED** (it was a hand-analysis error; the solver disproves it).
- **Only 3 configs are feasible**; **2 are Pareto-optimal**, and both **drop SD1** — the baseline
  (SD1=on) is dominated on pin-count. The real lever is SD1; audio must stay SAI5 (see next).
- **SAI7/SAI6 audio (the "P20-only" idea) is infeasible** *as currently modelled*: SAI7 speaker/mic
  need ENET pads already held by the control GPIOs (`OE_CAM`=RD3, `SYS_PRG#`=TXC, `OE_SOUND`=RD2).
- **C4 confirmed**: SD1 + I²C4-on-P20 conflict on ENET_RD0/RD1 → baseline's I²C4-on-P21 is correct.
- **Model caveat:** `control_sound` is modelled as a *fixed* pad-group. Those are relocatable GPIOs;
  if freed, SAI7 P20-only audio may become feasible. Refine the model (give control GPIOs options)
  before ruling SAI7 out — a solver is only as honest as its model.

## C1 (REFUTED): "the ENET1 block is over-subscribed → baseline infeasible"
- Claimed the baseline couldn't fit SD1 + SAI-TX on the 16 ENET pads. **Solver: FEASIBLE** — the
  assignment is exactly 16/16 with no conflict. Kept here as a record of a corrected error.
- Status: **rejected** (disproved by `solver/solve.py`).

## C2: the speaker SAI5-on-ENET mux is unverified → the baseline carries silent risk
- Objective stressed: risk / verification-debt
- Scenario: audio_speaker on the ENET pads.
- Baseline: labels ENET_RXC/RX_CTL/TD*/RD* as `SAI5_TX*` (per CompuLab Table 15).
- Dominating candidate: **cand-A** (SAI7 — RM-verified ALT2 on those pads) scores 0 risk; or keep SAI5 but **attach a verification** (CompuLab Q / BCLK scope).
- Tradeoff accepted: SAI7 gives only 1 TX data lane/SAI (see C3); staying on SAI5 keeps the risk until verified.
- Evidence: RM shows ENET balls → SAI6/SAI7 only (SAI5 has no dedicated TX pads); CompuLab Table 15 says SAI5_TX reaches them. Conflict unresolved on paper. P20.19 = 1.8 V + routing confirmed; instance not.
- Status: **open** — verification gates it (decision 2026-09-14: keep SAI5 pending proof).

## C3: SAI5 vs SAI6/7 is a real tradeoff — lanes vs locality/risk
- Objective stressed: discrete_lanes  ↔  locality + risk (tradeoff point)
- Scenario: 4-channel audio out.
- Baseline (SAI5): **4 discrete TX lanes on one SAI** (TXD0–3) — but spans P20+P21 and is unverified.
- Dominating candidate: **cand-A** (SAI7/SAI6): P20-only + RM-verified, but only **1 TX lane/SAI** (→ two SAIs + TDM for 4 ch).
- Tradeoff accepted: choosing SAI5 buys lanes at the cost of locality+risk; choosing SAI6/7 buys locality+risk at the cost of lanes. **No dominating winner** — this is the tradeoff the product must own.
- Status: **decided** — product = SAI5 (lanes win) unless verification fails; early bench = SAI6.

## C5: the current design puts 3V3 on the battery board → violates "1V8 everywhere" (2026-09-14)
- Objective stressed: **power_domain_purity** (hard, product profile)
- Decision: 1V8 everywhere on battery-driven boards; 3V3/5V only on the 5V input or on non-battery
  connector/module boards.
- Baseline (as drawn): `Faceboard/media-domain.kicad_sch` level-shifts the SAI5 bus through **3×
  TXS0104 (1.8↔3.3 V)** and routes 3V3 to the camera/M.2 module connectors (60-pin DF40 "202-SMART-
  CAM" `P7`); HDMI-DDC is 3V3 onboard too. These are **battery-board 3V3 nets → violations**.
- Dominating candidate: keep the **main (battery) board 1.8 V only** — move the level-shift + any 3V3
  DAC/codec to the **plug-in module side** (not battery-driven); offload HDMI to the USB-C host; keep
  audio 1.8 V-native (MAX98357A / SPH0645 / TAS-IOVDD amps — already recommended).
- Tradeoff accepted: the module boards carry the 3V3 domain + shifters; the main board stays pure 1.8 V.
- Evidence: KiCad `media-domain` (U19/U20/U21 TXS0104, 60p smart-cam DF40); contradicts the sound
  doc's "not level shifted" claim. **Now auto-detected** by `check.py` K3 (2026-09-15).
- Status: **open** — audit every battery-board 3V3/5V net against the decision (K3 flags the audio path;
  extend the K-series to the camera/M.2 sheets, which also carry TXS0104).

## C4: I²C4 (MCU bus) native pins collide with PCIe/ECSPI2
- Objective stressed: fault_isolation vs pin availability
- Scenario: mcu_control needs a dedicated I²C controller.
- Baseline: I²C4 on native P21.20/.24 — but those are PCIE_CLKREQ / ECSPI2_SS0 in the plan.
- Dominating candidate: I²C4 on **P20.21/.23** (freed if SD1 dropped, per cand-A), *or* drop PCIe+ECSPI2.
- Tradeoff accepted: either lose SD1, or lose PCIe/ECSPI2.
- Status: **open** — tied to C1 (the SD1 decision).

---

## Pugh matrix (vs current-plan = datum)

| Config | feasible | pins | locality | shifters | lanes | isolation | risk | verdict |
|---|---|---|---|---|---|---|---|---|
| **current-plan (SAI5)** | 0* | 0 | 0 | 0 | 0 | 0 | 0 | datum — *infeasible w/ SD1 (C1)* |
| cand-A (SAI7, no SD1) | + | + | + | 0 | − | 0 | + | Pareto — best if 2 lanes suffice |
| cand-B (SAI5, no SD1) | + | + | 0 | 0 | 0 | 0 | 0 | Pareto — keeps 4 lanes, still risk C2 |
| cand-C (SAI6 bench) | + | + | + | 0 | n/a | n/a | + | bring-up only, not a product config |

`*` current-plan is only feasible once SD1 is dropped/trimmed → then it becomes cand-B.

**Reading:** the plan's real fork is **SD1 (C1/C4)** and **SAI5-verification (C2)**. cand-A and cand-B
are the non-dominated options; the SAI5↔SAI6/7 choice (C3) is a genuine lanes-vs-locality tradeoff,
decided toward SAI5 pending the C2 verification.

**Next open decisions:** (1) is SD1 required? (2) SAI5 mux verification (CompuLab Q / BCLK scope).
