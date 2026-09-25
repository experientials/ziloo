# UCM-iMX8M-Plus pin-allocation evaluation

Structured, adversarial evaluation of the board's pin/bus allocation — to find where the current
plan is **suboptimal**, not just confirm it. Method (morphological design-space + ATAM challenges +
Pugh/Pareto scoring) is the **`pin-allocation-eval` skill**; this directory is the board's model +
data that the method operates on.

## Model layout & build step
The model is **layered across files** so multiple modules/boards/products can be tracked without one
giant file. `model.py` assembles a **product** from its parts; humans and tools consume the assembled
view, and every Markdown view is **generated** (`make render`). Never hand-maintain parallel tables
(that's what produced the C1 error). Format decision: **structured YAML in git + generated views** —
not hand MD tables (not machine-parseable), not `.mex`/DTS (tool-locked); those are *outputs*.

- **`common.yaml`** — shared `tag_vocab` + defaults (every product).
- **`modules/<m>.yaml`** — a component installed onto a host board (the UCM SoM): identity, install
  connectors (P1/P2), level domains. *What each ball CAN be* is bounded here.
- **`boards/<b>.yaml`** — a host **board**: its connectors, on-board chips, and per-pin allocation
  (`som · func · dest · alts · pad · tags`). **2-layer:** the chosen function lives on the board.
  `sb-ucm-carrier` (bench headers) and `929-faceboard` (DF40s + shifters) are two *different* hosts.
- **`products/<p>.yaml`** — a product = `modules:` + `boards:` (+ `kicad:` + product-only connectors
  like the draft product M.2). `ucm-bench` = SoM+carrier; `bob` = SoM+faceboard.
- **`model.py`** — `load_product(name)` merges the above into one flat view (errors on duplicate pins).
- **`render.py`** → `generated/<product>/` — per-connector tables, `sound_connector_cable.md`,
  `by_destination.md`, `by_tag.md`, `connectors.md`. **Do not hand-edit `generated/`.**
- **`solver/board.yaml`** — the formal feature→implementation model the CP-SAT validator selects over.
- **`schemas/pinmux.schema.json`** — JSON Schema (draft-07) for the module/board/product files:
  required fields, enums (`status`, `verified`), and `additionalProperties:false` so a **typo'd or
  unknown field is a hard error**, not silently ignored. Edit this when you add a field.
- **`check.py`** — per-product structural + reference + consistency + ground-truth cross-check.
  `S` validates every file against the schema (typos, missing-required, bad-enum). `N` validates
  **cross-file name references** — the ids in `product.modules/boards` and `board.hosts` are
  **filename stems** and must resolve to a real file/module (a broken ref is a hard error, not a
  crash). The registry `board:` field is **loader-derived** from the owning file, so it can't drift.
  `E*`/`W*` catch model self-inconsistency (SoM-ball reuse, pad↔connector drift, sound-connector
  completeness, tag vocab).
  `K*` compare against the product's **drawn KiCad schematic** (`kicad.schematic_dir`): K1 audio-bus
  presence, K2 sound-connector *planned vs placed*, K3 audio 1V8↔3V3 level-shift (C5), K4 connector-
  registry audit. Plan-vs-board drift is a **warning, not an error** — a board may lead or lag the plan.
  `F` is **connector fullness** — for a connector with `pins: N`, any of positions 1..N that has no
  modeled pin is a "hole" (warning). Acknowledge power/GND/NC via `power_pins: [..]`; set
  `complete: true` to promote a remaining hole to a hard error (used on the sound connector).
  Each product also prints an **`extent:`** line — a completeness/confidence report (pins verified
  vs unverified, connectors declared-but-empty *stubs*, registry status mix) so you can see how much
  is actually known vs stubbed/guessed.

**Known limits / future checks.** The `som` check validates *range* (P1/P2, 1..100), not the ball's
signal — catching a transposed-digit typo (`P2.53`→`P2.35`) needs the full P1/P2 ball→signal map
(hookups Table 44/45). An automated scrape of that PDF proved unreliable (≈85% of balls, per-ball
mux loss, mis-assignments), so it's deliberately deferred to a verified pass rather than shipped as
a false-positive-prone check.
- **`Makefile`** — `make check` (all products; `PRODUCT=bob` to scope one) · `make render` ·
  `make solve` (CP-SAT feasibility + Pareto + ledger) · `make all`.

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
