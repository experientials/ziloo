# Product audio architecture (decision 2026-09-20)

Sound in + out for the Ziloo/929 toy: **5-mic directional input + stereo speech output, M7-owned.**
Records the topology, chipsets, pin/SAI mapping, and why. Companion to `bench-v1.md` / `bench-v2.md`;
pin facts in `challenges.md` (C2 SAI map, C7).

## Decision

- **Analog mics = DEFAULT; digital MEMS = supported FALLBACK.** The central board supports **both** —
  mic technology is a **sound-board hardware config + firmware config**, not a fixed choice.
- Driver: the mics sit on **cloth extension points** (front/left/right/top [+ crown]), not a PCB.
  Analog = simple **differential, equal-length 10 cm** cable/flex (common-mode-rejecting + phase-
  matched) — far easier on fabric than routing a digital I²S bus + a mini-board to every mic. The
  differential + matched-length choice is what de-risks cloth-routed analog.
- **All audio on SAI3 → the ENET pads stay free** for debug / recovery / CI (their whole purpose).

## Signal chains

- **Analog (default):** `5 analog mics (differential, 10 cm matched) → multi-ch TDM ADC → SAI3 RX
  (1 line, TDM) → M7` ; `M7 → SAI3 TX → speaker amp → speaker`.
- **Digital MEMS (fallback):** `5 I²S/PDM MEMS mics → SAI RX (up to 4 data lines, or MICFIL/PDM) → M7`
  + the same speaker path.

## Central board — supports both

Route the FULL SAI to the sound-board connector: **MCLK · BCLK · LRCLK · TX_DATA · 4× RX_DATA**.
- Analog board uses **1 RX line (TDM)** from the ADC.
- MEMS board uses **up to 4 RX lines** (2 mics each).
- Firmware selects SAI **TDM (analog)** vs **multi-line I²S (MEMS)**. One connector, two boards, one flag.

## Chipsets

| Function | Part | Notes |
|---|---|---|
| **Mic ADC (analog)** | **TI TLV320ADC5140** | 4-ch differential analog **+ PDM**, integrated mic bias + per-ch PGA, TDM out, **cascadable to 8**. 1× = 4 mics; 2× = 5–8. Differential inputs reject the 10 cm-run noise; PDM support can also bridge toward the MEMS path. |
| **Speaker amp** | **MAX98357A** ×1–2 | I²S class-D, no MCLK, pin-strapped. **Shutdown gated by the MSP430** (per-channel enable): class-D idle draw (~2.4 mA/ch, confirm datasheet) must be gated for battery. Sequence enable-before-data to avoid turn-on pops. |
| **MEMS mics (fallback)** | ICS-43434 / SPH0645 (I²S), or PDM | validate on the same SAI later |

## Pin / SAI mapping

- **SAI3 pads** (product P1.26–38, **1.8 V native** — no shifter on the faceboard): full-duplex codec
  bus — **TXD → speaker**, **RXD → 5-mic TDM in**, shared BCLK/LRCLK/MCLK. All audio here.
- **ENET pads: NOT audio** — reserved for M7↔PC debug/recovery/CI (SAI6/7 excluded from the audio plan).
- Bench: the same SAI3 bus surfaces at **P21 (3.3 V** via the carrier's `I2S_LS_OE` shifter); the
  WM8731 (2-mic) or an ADC5140 breakout (5-mic) sits on it — see `spikes.md`.

## Ownership & power

- **M7-owned** (SAI3 + the ADC/amp control I²C); Linux gets audio over **RPMsg** (Track M).
- **MSP430 gates** the speaker-amp shutdown (per channel) + optionally the mic rail — battery power
  management — routed through the **SOUND/SUPERVISOR (SND_MOD)** connector.

## Open sub-decisions

- Mic count **4 vs 5** (front/left/right/top ± crown) → 1× vs 2× ADC5140.
- Speaker **2× mono MAX98357A vs 1× stereo class-D** (2 enable pins vs 1 — power/pin tradeoff).
- **AEC** (barge-in): use the digital I²S **TX stream as the reference** (no codec loopback needed).

## Validation

The one thing that could kill analog is channel noise/phase over the cloth runs under EMI. Gated by
**`spikes.md` SPIKE-2** (ADC5140 on SAI3, differential 10 cm runs, noise/phase with nRF + motor
running). Pass → analog confirmed; fail → MEMS fallback (already supported by board + firmware).
