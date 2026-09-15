# UCM-iMX8M-Plus pin-allocation evaluation

Structured, adversarial evaluation of the board's pin/bus allocation — to find where the current
plan is **suboptimal**, not just confirm it. Method (morphological design-space + ATAM challenges +
Pugh/Pareto scoring) is the **`pin-allocation-eval` skill**; this directory is the board's model +
data that the method operates on.

## Source of truth & build step
**`pins.yaml` is the canonical source** — humans and tools consume it, and every Markdown view is
**generated** from it (`make render`). Never hand-maintain parallel tables (that's what produced the
C1 error). Format decision: **structured text (YAML) in git + generated views** — not hand MD tables
(not machine-parseable), not `.mex`/DTS (tool-locked / intent-poor); those are *outputs*, not source.

- **`pins.yaml`** — canonical per-pin allocation (P20/P21/P10): som · function · destination · alts ·
  verified · level. Edit here.
- **`render.py`** → `generated/` — `P20.md`, `P21.md`, `P10.md`, `sound_connector_cable.md`,
  `by_destination.md`, `by_tag.md`, `connectors.md` (connector registry). **Do not hand-edit `generated/`.**
- **`solver/board.yaml`** — the formal feature→implementation model the CP-SAT validator selects over.
- **`check.py`** — consistency + ground-truth cross-check. `E*`/`W*` catch YAML self-inconsistency
  (SoM-ball reuse, pad↔connector drift, sound-connector completeness, tag vocab). `K*` compare the
  model against the **drawn KiCad schematic** (`meta.kicad.schematic_dir`): K1 audio-bus presence,
  K2 sound-connector *planned vs placed*, K3 audio 1V8↔3V3 level-shift (challenge C5). Plan-vs-board
  drift is a **warning, not an error** (exit 0) — the board may legitimately lead or lag the plan.
- **`Makefile`** — `make check` (consistency + KiCad K-series) · `make render` (regen views) ·
  `make solve` (validate + Pareto + ledger) · `make all`.

## Evaluation files
- **`model.yaml`** — descriptive resources/features/constraints/objectives/profiles (design doc).
- **`configs.yaml`** — baseline + candidate allocations.
- **`challenges.md`** — ATAM challenge log + Pugh matrix (now cross-checked by the solver).
- **`solver/solve.py`** + **`solver/ledger.json`** — the CP-SAT validator and its objective ledger.

Related design docs: audio in [`909c/BRIDGE_BOARD_SOUND.md`](909c/BRIDGE_BOARD_SOUND.md).

## Current headline findings (see `challenges.md`)
1. **ENET1 block over-subscribed** — baseline is infeasible with SD1 *and* SAI-TX (C1); real fork is
   whether SD1 is needed.
2. **SAI5-on-ENET mux unverified** — carries silent risk vs RM-verified SAI6/SAI7 (C2).
3. **SAI5 vs SAI6/7** = a genuine lanes-vs-locality tradeoff (C3) — decided toward SAI5 pending C2.
4. **I²C4 MCU bus** native pins collide with PCIe/ECSPI2 (C4) — tied to the SD1 decision.

## Targets (board variants)
`model.yaml` is the **UCM-iMX8M-Plus** target. `features`, `objectives`, and `profiles` are
board-independent (the wishes and scoring axes are shared); only **`resources`** (the pad×ALT×
connector set) differ per module. When the smaller Compulab cousin (fewer pins) is planned, add its
resources as `model.<cousin>.yaml` (or a `targets:` block) reusing the shared features/objectives/
profiles, and score configs per **(target × profile)**. A feature set that stays feasible on the
smallest target is the portable core; where the cousin runs out of pins is exactly where the
adversarial evaluation matters most.

## Scale up later
Encode `model.yaml` for **CP-SAT / MiniZinc** to auto-check feasibility, compute the Pareto front,
and auto-generate challenges; or import into **NXP MCUXpresso Pins Tool** for the feasibility/DTS
layer. See the skill's *Scale up later* section.
