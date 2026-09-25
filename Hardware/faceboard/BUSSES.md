## Busses going through the Faceboard

- [Stem I2C](../stem/README.md) is primarily used to communicate between MCUs that can pass master role between them
- Day I2C is Sensor I2C on the Left Camera?
- Night I2C is Sensor I2C on the Right Camera?
- SYS I2C is mastered by the SoM while awake to control PCIe, RT Clock, and PMIC.
  - **Clarification (2026-09-24):** SYS_I2C is **SoM-side only** — the **MSP430 supervisor is never on
    it** (the MSP is on **Stem + Sensor only**; see `../stem/STEM-EXPANDER.md`). Two contexts share the
    name: on the **product faceboard**, SYS is the superset that includes the PMIC (PCA9450 @0x4A/0x4B)
    per `../pinouts/SYS_I2C_ADDRESSES.md`; on the **CompuLab bench carrier**, SYS_I2C = the SoM's
    **I²C2** (RTC/EEPROM/codec) and the **PMIC is on I²C1**, a separate bus (`../pinmux/challenges.md`
    C6, hardware-verified 2026-09-19). Master model for the MCU buses: **Stem = always SoM-mastered**
    (MSP always slave); **Sensor = switches masters** (MSP in Sensing / SoM in Passive).
- Host USB 3.0 connects to T-USB Host by default, but can be switched to M.2 Key B connection by M2B_USB_MUX(set High).
- Host USB 2.0 connects to T-USB Host by default, but can be switched to M.2 Key B connection by M2B_USB_MUX(set High).
- Host USB 2.0 defaults to M.2 connector, but can be switched to 50 pin connector
- Should OTG USB 2.0 optionally be routed to Key E ?
- PCIe(PExx0) single lane to M.2 Key B
- 4 channel SAI5/I2S stereo input
- 4 channel SAI5/I2S stereo output
- PCA9555 I/O Expander #0 for compatibility with default Yocto firmware
- Stereo Audio to M.2 Key B
- SDIO2 to M.2 Key B
- ECSPI2 MISO/MOSI
- DAS/DSS broken out with activity LED + SAI5 clock
- SIM card isn't currently supported
- GNSS on M.2 module would be accessed via Stem I2C

SD1 connects to (embedded module? and) M.2 Key E
SD2 connects to SD Card slot and M.2 Key B



### Switching busses on/off

- SN74CB3Q3125 in stock (SN74CB3Q3125PWR SMD TSSOP 14 or SN74CB3Q3125DBQR SMD SSOP 16)
- TMUX1511 not in stock
- A SN74CB3Q3245 is used to connect Expander firmware programming pins during programming mode



### UARTS

UARTS 2 and 4 is connected to Firmware upload pins on Faceboard Expander and T-USB Expander when 
System Programming Mode is set, which is done by setting SYS_PRG# to LOW.

Otherwise UARTS 2 and 4 are reserved for debug output from SoM cores.

- UART1 connected to UART_T_*XD on 50 pin T-USB connector and to SoM
- UART2 connects M.2 Key B BT/LPWAN UART and to SoM, is also used for A53 core debug
- UART3 connected to UART_F_*XD on Faceboard Extender and to SoM.
- UART4 is reserved for M7 core debug


### Sound I2S

Sound is managed from the SoM an uses 1.8V. It is switched off if OE_SOUND pin is set to LOW.
The sound bus is routed to M.2 Key B, Sound Connectors and Camera Modules.
