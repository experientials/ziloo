SYS I2C addresses

> **Scope — CANONICAL (2026-09-24).** SYS_I2C is the **SoM-side system bus**: the SoM masters it while
> awake for its own system devices (RTC, EEPROM, codec, and on the product faceboard the PMIC/PD/clkgen/
> expanders in the table below). The **MSP430 supervisor is NOT on this bus** — the MSP is on **Stem +
> Sensor only** (see `../stem/STEM-EXPANDER.md`). This table is the **product-faceboard superset**; the
> **CompuLab bench carrier** populates a subset on the SoM's **I²C2** (RTC/EEPROM/codec), with the
> **PMIC on I²C1** there (`../pinmux/challenges.md` C6, hardware-verified). The old "unified I2C" idea
> (SYS+Stem+Sensor on one bus) is **dead**.

<mark>Reduced the devices connected to SYS bus</mark>

| Address    | Chipset  | Description               |
|------------|----------|---------------------------|
| 0x20       | PCA9555  | 16 bit expander EX0       |
| 0x25       | PCA9450  | Reserved 7 bit address    |
| 0x26       | PCA9555  | 16 bit expander EX6       |
| 0x4A 0x4B  | PCA9450  | Power Management IC       |
| 0x68       | PI6CG18200 | PCIe clock generator    |
| 0x70 0x71  | TPS65988 |  RESERVED for PD Controller Port 1 / SYS |
| 0xD2/D3    | RTC      | AM1805 real time clock (RTC) |

