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

## C2 (RESOLVED 2026-09-18): SAI5 is NOT on the ENET pads — the CompuLab doc was wrong
**Authoritative source:** NXP `imx8mp-pinfunc.h` (lf-5.10.y). Every ENET pad's SAI mux was read
directly:
- **ENET pads mux to SAI6/SAI7 only, never SAI5.** `ENET_RXC→SAI7_TX_BCLK`, `ENET_RX_CTL→
  SAI7_TX_SYNC`, `ENET_TXC→SAI7_TX_DATA00`, `ENET_RD3→SAI7_MCLK`; `ENET_MDC/MDIO/TD3/TX_CTL→SAI6_TX*`.
  CompuLab Ref-Guide Table 15 (SAI5_TX on ENET) is **wrong** — no SAI5 macro exists for those pads.
- **SAI5 IS available, on different pads:** `SAI5_TX*` = the **SAI2_* pads** (SAI2_RXC=TX_BCLK,
  RXFS=TX_SYNC, RXD0/RXFS/TXC/TXD0 = TX_DATA0–3, SAI2_MCLK) → **4 discrete TX lanes**; `SAI5_RX*` =
  the **SAI3_* pads** (4 RX lanes). So the model's *mic* mapping (SAI5_RX on SAI3/P21) was correct;
  the *speaker* mapping (SAI5_TX on ENET) is wrong and must move to the **SAI2 pads** (P21 CAN pins).
- **Bench consequence:** the MAX98357A wired on ENET_RXC/RX_CTL/TXC is **SAI7** (1 lane), not SAI5.
- **Model fix owed:** flip `SAI5_TXD*/TXC/TXFS` on the ENET/P20 pins → SAI2-pad locations, or relabel
  the ENET block as SAI6/SAI7. Until then the `SAI5_TX`-on-P20 pins in `pins.yaml` are known-wrong.

## C3 (REFRAMED 2026-09-18): the SAI choice is an audio-ARCHITECTURE decision, not just lanes
With authoritative pad data, the real fork is **density vs domain-separation**:
- **SAI5 = density.** One SAI, shared clocks, **4 TX + 4 RX** discrete lanes → 4 spk + 4 mic, fewest
  pins, **one owner (Linux/A53)**. Uses SAI2 pads (TX, = P21 CAN pins) + SAI3 pads (RX, = P21 mic).
- **SAI6 + SAI7 = separation.** Independent SAI instances → **different masters**: speaker on
  Linux/A53 (one SAI), **mic on the Cortex-M7 real-time core** (the other SAI, via RDC + rpmsg —
  infra already on this board, `0004-...rpmsg` patch). Decoupled clocks/software/failure; always-on
  low-latency capture independent of Linux. Cost: more pins, 1 lane each (or TDM). ENET block, P20.
- **Decision driver:** does mic capture need real-time/isolated M7 ownership → split SAI6/SAI7; or is
  a unified Linux 4-in/4-out pipeline enough → SAI5 (densest). Fast bench beep = SAI7 (current wiring).
- **FINDING (2026-09-18, AUTHORITATIVE — `imx8mp-pinfunc.h` × CompuLab Ref-Guide Table 44/45 read
  page-by-page): SAI5 SPEAKER is physically impossible on the SB-UCM carrier — no frame-sync pin.**
  - SAI5_TX needs LRCLK. pinfunc gives `SAI5_TX_SYNC` only on the **`SAI2_RXFS`** (or dedicated
    `SAI5_RXD1`) pad — and **neither is broken out** on P1/P2. CompuLab's hookup maps `SAI5_TXFS`
    onto **P2.53 = `ENET_RX_CTL`**, which pinfunc says is `SAI7_TX_SYNC` — impossible for SAI5. So
    the CompuLab SAI5_TX-on-ENET labels are a *fudge for the missing SYNC pad*, not a real option.
  - What SAI5_TX *does* have broken out: BCLK (`SAI2_RXC`=P1.53), 2 data lanes (`SAI2_TXC`=P1.51,
    `SAI2_TXD0`=P1.33), MCLK — but **no SYNC** → no I²S TX. Dead end.
  - **Speaker ⇒ SAI6 or SAI7** (ENET/P20): the only pads with a complete, pinfunc-valid
    BCLK+SYNC+DATA0. The bench MAX98357A wiring is already SAI7. Multichannel = TDM or SAI6+SAI7.
  - **Mic ⇒ SAI5_RX** (SAI3 pads, P21): fully broken out (RXC=P1.32/89, RXFS=P1.34/87, RXD0-3 on
    P1.28/38/36/26, MCLK) → up to 4 channels. **The model's mic mapping was correct.**
  - **CAN is freed of the conflict** — the SAI2 pads were never a viable speaker path, so keep
    CAN1 and/or CAN2 as desired at **zero cost to audio**. (Supersedes the earlier CAN1-vs-CAN2
    analysis, which rested on the wrong premise that SAI5-TX-on-SAI2 was usable.)
  - **Model fix owed:** relabel the ENET/P20 `SAI5_TX*` pins as **SAI6/SAI7** (their only real
    audio function); the `SAI5_RX` mic pins on SAI3/P21 stay as-is.

## C6 (RESOLVED 2026-09-19): the SB-UCM carrier is a CompuLab board — this model is a PLAN; SYS_I2C = I²C2, not I²C3
Prompted by a bench misadventure: I treated `sb-ucm-carrier.yaml` as fact and conflated the Talki
`SYS_I2C` bus onto the eval carrier. Corrected against the **official CompuLab docs**:
- **Authority split.** The SB-UCM-iMX8Plus carrier is **CompuLab's**, not ours → its facts (pin
  functions, what's on a bus, boot flow) come from CompuLab's **reference guide / P1-P2 hookups /
  carrier design package**. `boards/sb-ucm-carrier.yaml` is **our intended allocation — a PLAN** — and
  must be validated against those docs, not read as truth. (Header note added to that file.)
- **SYS_I2C = I²C2**, NOT I²C3. Ref-Guide Table 27: `I2C2_SCL=P1-99`, `I2C2_SDA=P1-97`, and the note
  *"I2C2 is the system I2C channel … RTC, EEPROM."* The multifunctional table confirms P1-97/99 =
  `SYS_I2C_SDA/SCL`. **I²C3** (Table 28, P1-91/94) is a plain **general-purpose** bus.
- **`SYS_I2C_ADDRESSES.md` is the TALKI FACEBOARD superset; a SUBSET of its devices is on the bench.**
  Real, *responding* devices on **I²C2** (verified 2026-09-19): `wm8731` codec (0x1a), `24c08` EEPROMs
  (0x50/0x54, read the SoM board-ID), `ab1805` RTC (0x69), +0x67. The SYS **I/O expander
  (`pca9555 @0x20`) is NOT populated** — it's a phantom driver bind (dmesg `1-0020: -ENODEV`); the
  expanders + TPS65988 PD + PI6CG18200 clkgen are **faceboard** parts. `UU` in i2cdetect ≠ a real chip
  (verify with dmesg / `i2cget -f`).
- **Verified on hardware (2026-09-19):** real SYS devices (codec/RTC/EEPROM) are on **I²C2**, not I²C3.
  **I²C3** (`i2c-2`) enables cleanly (proved the DT loop) but has **no real device** — its `pca6416@20`
  is the same phantom bind (`2-0020: -ENODEV`, `i2cget -f`→0xff); it's a free GP/sensors bus on
  P20.33/.34, **kept enabled**. **Real I²C comms confirmed** by reading the 24c08 EEPROM over I²C2
  (returned the SoM board-ID). A DT node ≠ a real chip.
- **Consequence:** don't spike on I²C1 (PMIC) or I²C2 (SYS_I2C, reserved); I²C3 is a fine
  general-purpose bus. DT-config/boot mechanism (no runtime overlays; `fw_setenv` broken; edit the
  booted variant on `mmcblk2p1`) is captured in the `ucm-dev` skill `references/devicetree-config.md`.

## C7 (2026-09-20): BLE radio (nRF52840) on ECSPI2 + bench sound/BLE coexistence
- **Radio transport = ECSPI2** (SoM P2.89/91/93/95; bench P21.22/24/26/28). **Unallocated in the
  product** (`bob.yaml`/`929-faceboard.yaml`) — only the carrier earmarks it "future sound", so it's
  **free for a `BLE_MOD`** (nRF52840 as NCP, M7-owned). Claiming it retires the dormant
  I²C4-native-on-P2.91 option (see C4). USB is the *bench* transport (DFU-programmable), SPI the
  *product* one; radio kept an omittable module. BLE-HCI-over-SPI is **not** a standard BlueZ
  transport → SPI carries NCP/Thread-RCP, not raw HCI. Architecture: `ucm-dev/m7-coprocessor.md`.
- **Bench coexistence on P21 (verified from the pin map):**
  - **BLE (ECSPI2, even .22–.28) + mic array (SAI5 RX, odd .11–.23): coexist** — different pins,
    peripherals, pads; one dtb enables both. This is the beamforming-input + radio bench.
  - **A speaker does NOT fit on P21 alongside BLE:** SAI7-speaker lands on the ECSPI2 pins
    (.22/.26/.28 SAI7 alts) → collides with BLE; the WM8731 analog jack (SAI3) lands on the mic pads
    (.11–.23) → collides with the digital mic array. Route the speaker **off** P21.22–28: SAI7 on the
    P20 ENET pads (drop eth0 → USB-GbE), SAI5_TX on the SAI2 pads (C2-corrected, unverified), or USB
    audio. Practical: a **"BLE + mic-array"** config, speaker tested separately / off-P21.

## C2-orig: the speaker SAI5-on-ENET mux is unverified → the baseline carries silent risk
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

## SD1 — why it's here (history) & the drop decision (2026-09-15)
- **Question raised:** "Why did I add SD1? A second SD *card* slot is useless." (Henrik, 2026-09-15)
- **Correction — SD1 is not a card slot; it's the SDIO bus for the M.2 Key-E wireless module.**
  `pinouts/M2_KEY_E_CONNECTOR.md` maps Key-E pins 9/11/13/15/17/19 → `SD1 CLK/CMD/DATA0-3`, pin 23 →
  `SD1_RESET_B`, and states *"Supports WNFB-266XI SDIO Wireless Module via SoM (SD1, UART2)."* On the
  carrier, SD1 is dual-muxed onto the ENET1 pads (`ENET1_RD0/SD1_DATA2` … in `sb-ucmimx8plus_1v1`).
  So SD1 = **WiFi/BT SDIO transport**, the reason it was reserved.
- **What dropping SD1 actually costs:** not a redundant card slot — it removes the **SDIO path for
  Key-E WiFi/BT**, forcing wireless onto **USB2 and/or PCIe via M.2 Key B** (COEX/USB, per
  `M2_KEY_B_CONNECTOR.md`). If the product commits to Key B for wireless (current draft M.2 plan is
  Key B), SD1 is genuinely free to drop → the ENET1 block opens up for SAI/I²C (the solver's main
  lever: dropping SD1 is the only path to the Pareto-optimal configs; see automated validation above).
- **One controller, mutually exclusive (Henrik, 2026-09-15):** SD1 = the SoM's single **uSDHC1**.
  It is **SD card XOR SDIO-wireless — never both at once.** Accepted position: *"if we use SDIO for
  wireless, I can live without a working SD-card slot."* Optional refinement: a **mux/switch to select
  SD-card vs SDIO-wireless** on the shared bus (only one active at a time; adds a control GPIO + a
  2:1 switch — worth it only if both a card slot and SDIO wireless must physically coexist).
- **Carrier vs product nuance:** on the **SB-UCM carrier**, the M.2 (P9) does wireless over **USB2/
  USB3/PCIe — not SDIO** (SD1 there is free for a card). **SDIO-wireless is specifically the product /
  M.2 Key-E path** (`M2_KEY_E`). So "SD1 for wireless" only bites on the product, not the bench.
- **Decision:** *lean drop on the product*, **gated on the wireless transport choice.** Keep SD1 iff
  Key-E SDIO wireless stays in scope (then no SD card, or add the mux); drop it once wireless is
  confirmed on Key-B USB/PCIe. Tied to the M2_PRODUCT keying (still `draft`/TBD) — resolve together.

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
