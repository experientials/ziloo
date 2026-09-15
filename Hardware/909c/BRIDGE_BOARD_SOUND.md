
# Sound 

The board maps SAI3 and ENET1 pins to SAI5 input and output with a full 4 channels. 
The Master clock pin is available, but is not used.
The signals are immediately mapped to 1.8V, which is then routed to the Camera Modules, the M.2 connector and Sound Connectors.


### Camera Connector mapping (SAI5)

| pin | code       |          |                                      | signal |
|-----|------------|----------|--------------------------------------|------|
| 14  | BCLK / SCK | I2S      | Bit clock line - P1.32 SAI5_RXC      | 1.8V |
| 15  | WS / LRCLK | I2S      | Word clock line - P1.34 SAI5_RX_SYNC | 1.8V |
| 16  | SDATA1     | I2S      | Input data 1 - P1.38 SAI5_RX_DATA1   | 1.8V |
| 17  | SDATA2     | I2S      | Input data 2 (NC)                    | 1.8V |


### Supervisor Connector mapping (SAI5)

<mark>This has been revised</mark>


| Pin id.	| Upper     | Lower      | Description                        | Counterpoint   | Voltage Level | Spec Feature |
|-----------|-----------|------------|------------------------------------|----------------|---------------|--------------|
| 10        | 	        | LED_1      | GPIO9 / WWAN LED_1 / BCLK / SCK    | SAI5_TXC/P2.55 | 3.3V          |
| 20        |           | M2_I2S_TXFS| GPIO5 / SPK I2S LRC                | SAI5_TXFS/P2.53| 1.8V          |
| 22	    |           | M2_I2S_TXD0| GPIO6 / SPK I2S DAT                | SAI5_TXD0/P2.60| 1.8V         |
| 24	    |           | M2_I2S_RXFS| GPIO7 / MIC I2S LRC			      | SAI5_RXFS/P1.34| 1.8V         |
| 26	    |           | GPIO10     | SOUND_INT?                         | INT pin?       | 1.8V         |
| 28        |           | M2_I2S_RXD0| GPIO8 / MIC I2S DAT			      | SAI5_RXD0/P1.28| 1.8V         |

The GPIO10 / SOUND_INT is not yet confirmed.


### I2S (SAI5) 4 channel microphone input mapping

One lane goes to the 34 pins camera connectors
The microphones on the 34 pins connector use SAI5_RX_DATA0.

The full 4 lanes are available on the sound connector and M.2 Key B.


#### Microphone I2S mapping (SAI5)

The microphone I2S mapping is done by using AL2 mode for the SAI3 pads to get SAI5 signals.
[Multiplexed Signal Pins](./ucm-imx8plus_multifunctional.pdf). 
This provides the 4 microphone lines on the Sound Connector.

| Misc pin | SoM pin | i.MX pad      | Functionality     | ALT       | I2S                |
|----------|---------|---------------|-------------------|-----------|--------------------|
| 11       | P1.26   |  SAI3_TXD     |  SAI5_RX_DATA3    | ALT2      |      |
| 17       | P1.28   |  SAI3_RXD     |  SAI5_RX_DATA0    | ALT2      | DATA0    |
| 15       | P1.30   |  SAI3_MCLK    |  SAI5_MCLK        | ALT2      |      |
| 19       | P1.32   |  SAI3_RXC     |  SAI5_RXC         | ALT2      | BCLK    |
| 23       | P1.34   |  SAI3_RXFS    |  SAI5_RX_SYNC     | ALT2      | LRCLK    |
| 13       | P1.36   |  SAI3_TXC     |  SAI5_RX_DATA2    | ALT2      |      |
| 21       | P1.38   |  SAI3_TXFS    |  SAI5_RX_DATA1    | ALT2      |      |


#### Speaker I2S mapping (SAI5)

ENET1 are mapped as SAI5 and brought out as speaker on 20 pins Sound connector.
[Multiplexed Signal Pins](./ucm-imx8plus_multifunctional.pdf).

> ⚠ **Open verification:** confirm SAI5_TX actually muxes onto these ENET pads — CompuLab Table 15
> says it does; the NXP RM suggests these balls carry SAI6/SAI7. **Product plan stays SAI5** (4
> discrete TX lanes vs 1/SAI). See *Bring-up findings* below.

| Misc pin | SoM pin | i.MX pad              | Functionality           | I2S |
|----------|---------|-----------------|-------------------|-----------|--------------------|
| 15       | P1.30   |  SAI3_MCLK      |  SAI5_MCLK        | ALT2      |      | 
|          | P2.53   | ENET1_RX_CTL    | SAI5_TXFS         | ALT       | LRCLK     |
|          | P2.55   | ENET1_RXC       | SAI5_TXC / BCLK   | ALT       | BCLK     |
|          | P2.60   | ENET1_TD0       | SAI5_TXD0         | ALT       | DATA 0    |
|          | P2.63   | ENET1_TD2       | SAI5_TXD2         | ALT       |      |
|          | P2.65   | ENET1_TD3       | SAI5_TXD3         | ALT       |      |
|          | P2.76   | ENET1_nRST IO24 | SAI5_TXD1         | ALT       |      |


## Sound connector 20 pins

<mark>The sound connector is new, it replaces the 6 pin</mark>

The sound connector provides 4 lines input and 4 lines output. They connect
directly to the System Module, so they are not level shifted.
The signal level is **1.8V** (NVCC_SAI) — confirmed on hardware, see *Bring-up findings* below.
The pin layout wraps around aligning 1 and 20 close, but on opposite sides.

Two Connector components used are [DF40HC(3.5)-20DS-0.4V(51)](https://www.hirose.com/en/product/p/CL0684-4188-0-51). [Socket @ Mouser](https://www.mouser.ch/ProductDetail/Hirose-Connector/DF40HC35-20DS-04V51?qs=sGAEpiMZZMtJbfcMcIM8CC3aG3XFbLOWRtCXQ0n%252BY5Y%3D)
It is the same Hirose DF40 family — 0.4 mm-pitch SMT board-to-board (mezzanine) — as the UCM SoM
connectors (`DF40HC(3.0)-100DS`), just 20-pin / 3.5 mm stack. Not hand-solderable; it stacks a board,
it does not cable out to a ribbon.

> **Planned ≠ built (verified 2026-09-15, `pinmux/check.py` K2).** This dedicated, unshifted 1.8 V
> 20-pin sound connector is the *plan*. On the current `929/Faceboard` it is **not placed**
> (`sound.kicad_sch` is empty; only 100/60/50/34DS DF40s exist). Audio today rides the **60-pin
> smart-cam DF40** on `media-domain`, **through 3× TXS0104 (U19/U20/U21) 1.8↔3.3 V shifters** — so
> the "not level shifted" statement above describes the *target*, not the as-drawn board (that shift
> is the 1V8-everywhere violation, challenge C5).

:[Sound Connector](../pinouts/SOUND_CONNECTOR.md)


## Bring-up findings & component decisions (2026-09)

Recorded from dev-board bring-up on the SB-UCM-iMX8Plus carrier (non-'E' module). Resolves the
"1.8V or 3.3V — not yet defined" question above and flags a SAI-instance caveat on the speaker map.

### ✅ Signal level confirmed = 1.8V
Drove `ENET_RX_CTL` (P2.53) as `GPIO1_IO24` and measured **P20.19 = 1.9V** (1.8V domain, light-load;
toggles cleanly to ~0V). So `NVCC_SAI` = **1.8V** — the "not yet defined" note above is resolved.
This also confirms the **P2.53 ↔ P20.19** carrier routing.
Method (no `devmem` on the image): `python3` `mmap` `/dev/mem` IOMUXC `0x30330000`, write the pad
`SW_MUX_CTL = 0x5` (ALT5 = GPIO), drive via sysfs `gpiochip0` (base 0). ENET mux offsets:
`MDC 0x40, MDIO 0x44, TD3 0x48, TD2 0x4C, TD1 0x50, TD0 0x54, TX_CTL 0x58, TXC 0x5C, RX_CTL 0x60,
RXC 0x64` (mis-hitting 0x58/TX_CTL gives a false 0V).

### SAI5 (product) vs SAI6 (early bench) — one open verification
**Product plan stays SAI5** (decision 2026-09-14): it gives **4 discrete TX lanes on one SAI**
(TXD0–3) + 4 RX lanes, vs **1 TX lane per SAI** on SAI6/SAI7 — so no real loss, and **CompuLab
Ref-Guide Table 15** backs it (SAI5_TX on P2-53/55/60/63/65/76). **One open item:** the NXP i.MX8MP
RM shows those ENET balls mux to SAI6/SAI7 (SAI5 has *no dedicated TX pads*), so **verify SAI5_TX
actually muxes on the ENET pads** — via the CompuLab question below or a BCLK scope. Fall back to
SAI6/7 **only if** it can't. Confirmed so far: **P20.19 = 1.8 V, P2.53↔P20.19 routing**.

**Early bench testing uses SAI6** (its TX lands cleanly on P20, easy MAX98357A wiring):
`ENET_TD3`=BCLK **P20.28**, `ENET_MDIO`=LRCLK **P20.17**, `ENET_MDC`=DATA0 **P20.15**,
`ENET_TX_CTL`=MCLK **P20.20** — all **ALT2**. (SAI7 alt, if preferred: BCLK P20.29, LRCLK P20.19,
DATA0 P20.30.)

Candidate speaker-TX pins (for the BCLK-scope verification of the product SAI5 path):

| Header | SoM | ENET pad | mux off | GPIO1_IO | CompuLab / RM label |
|---|---|---|---|---|---|
| P20.19 | P2.53 | ENET_RX_CTL | 0x060 | 24 | SAI5_TXFS / SAI7_TX_SYNC ✅measured |
| P20.29 | P2.55 | ENET_RXC | 0x064 | 25 | SAI5_TXC / SAI7_TX_BCLK |
| P20.30 | P2.69 | ENET_TXC | 0x05C | 23 | SAI7_TX_DATA0 |
| P20.26 | P2.63 | ENET_TD2 | 0x04C | 19 | SAI5_TXD2 / SAI6_RX_DATA0 |
| P20.28 | P2.65 | ENET_TD3 | 0x048 | 18 | SAI5_TXD3 / SAI6_TX_BCLK |

### Sound-connector cable → carrier header (dev-board wiring)
To recreate the 20-pin DF40 sound connector (`../pinouts/SOUND_CONNECTOR.md`) from the SB-UCM P20/P21
headers — the wire list for the extraction cable (product SAI5 path):

**Table:** generated from `pins.yaml` →
[`pinmux/generated/sound_connector_cable.md`](../pinmux/generated/sound_connector_cable.md) (16
signal pins; rebuild with `make -C ../pinmux render`, cross-check `make -C ../pinmux check`).

Notes: the plan does not number the header **power/GND** pins (DF40 1/9/10/20) — identify 5V/3V3/GND
on P20/P21 physically before wiring them. Signals are **1.8V** (SPK/MIC + I2C6); keep leads short.
Speaker on P20, mic + I2C6 on P21 — the cable spans **both headers**. (For SAI6 early-bench, speaker
moves to P20.28/17/15 — see below.)

### P20-only sound connector (via SAI6/SAI7)
All ENET pads break out on **P20**, and SAI6+SAI7 (both TX and RX) live entirely on ENET pads — so
**speaker *and* I²S mic fit on P20 alone** if we use SAI7/SAI6. The **SAI5** route needs P20 (TX) +
**P21** (mic RX, on the SAI3 pads). A module *codec* still needs I²C6 (P21); a dumb amp + I²S mic
does not. (Header power measured on P20: **5V, 3V3, GND — no 1.8V**.)

### Amp selection
- **Bench (SAI6, early test):** on-hand **MAX98357A** direct — V_IH ~1.4V takes 1.8V I²S with **no
  level shifter, no MCLK**. Wiring (all ALT2): BCLK→**P20.28**, LRC→**P20.17**, DIN→**P20.15**,
  VIN→5V/3V3, GND. Stereo = 2× (each strapped L/R via SD).
- **Product:** prefer an amp with a **1.8V IOVDD/DVDD** pin so the bus stays 1.8V native and the
  TXS0104 shifters can be **deleted**: **TAS5805M** (stereo 23W, I²C+DSP), **TAS2780/2770** (mono
  smart amp), or **ES8311** (codec+amp, if a mic is also wanted).

### Level shifters (only if a 3.3V amp / 3.3V module connector is used)
Use a **directional push-pull** translator — SN74LVC2T45 / **SN74LVC8T245** / TI TXU0304/0104 —
**not** TXS0102/04/08 (pass-gate, I²C-oriented, unreliable push-pull) and **not** BSS138 discrete
boards (too slow for MHz clocks). TXB0104/0108 (Adafruit #1875/#395) are easy auto-dir breakouts and
work into a high-Z amp input. **NB:** the 929 Faceboard `media-domain` currently uses **TXS0104** on
the sound nets — a directional part fits a fixed-direction I²S bus better; revisit.

### Mic — SPH0645 I²S MEMS, direct at 1.8V
Supply **1.6–3.6V**, I²S slave, **I/O tracks VDD** (Adafruit breakout has no regulator). **Power it
at 1.8V** → `DOUT` to the chosen SAI's RX data pin, sharing BCLK/WS with the speaker (full-duplex);
no shifter. Early-bench (SAI6): `DOUT`→**P20.26** (`SAI6_RX_DATA0`). Product (SAI5): mic RX is on
**P21** (SAI5_RX, see the mic mapping above). **⚠ Never power at 3.3V** — 3.3V DOUT exceeds the 1.8V i.MX pad's abs-max, and 1.8V clocks
fail the mic's VIH at 3.3V VDD. P20 has no 1.8V pin, so add a small **3V3→1.8V LDO** (600 µA) for the
mic rail — still a P20-only connector, plus one LDO. SPH0645 has the known 24-bit-in-32-bit-frame /
MSB-delay quirk — a solved `simple-audio-card`/`dai-format` config.

### Linux driver support
`fsl_sai` drives any SAI (5/6/7) as an I²S master TX; `CONFIG_SND_SOC_MAX98357A=m` is already in the
CompuLab BSP config. Wire-up is device-tree only: a `simple-audio-card` on the proven `&saiN` + a
codec node (copy the wm8731/SAI3 pattern in `meta-bsp-929/.../0003-...Add-device-trees.patch`). For a
**zero-wiring smoke test of the audio software stack**, enable the eval carrier's own **WM8731 on
SAI3 → analog jacks** via the `0017-...-Add-ucm-imx8m-plus-wm8731.dts.patch` variant.

### Open — CompuLab support question (paper arbiter for SAI5-vs-SAI7)
For the non-'E' `UCM-iMX8PLUS-C1800Q-D1-N16`: (1) which i.MX8MP ball is bonded to each of
P2-60/76/63/65/55/53; (2) is SAI5 TX reachable on those pins per Table 15 and via which IOMUX ALT, or
do the signals emerge as SAI6/SAI7; (3) is there a machine-readable ball↔pin↔ALT table; (4) confirm
the RGMII/ENET1 balls are free on the non-'E' module.

*(Dev-board bring-up steps are tracked in the `ucm-dev` skill roadmap, task C6.)*
     

