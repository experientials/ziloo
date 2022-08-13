# M.2 Supervisor Slot

Ziloo has an M.2 slot for adding a remote control Wide WAN card.
With this card you can,

- Keep Ziloo updated with Security Fixes
- Track Ziloo with Global Positioning
- Monitor that Ziloo is functioning
- Remotely wake/suspend Ziloo
- Expand the storage for recordings
- Speaking through BT Speakers

The supervisor potentially has the following modules,

- WWAN LoRa
- NVMe SSD
- nRF53 Thread/BT module
- RP2040

It could have LTE module, but that seems $100 vs $15 for LoRa modules, and it would require a fee to networks.
GNSS / GPS module could be added to provide global positioning, it can be exposed on I2C. This would be managed by a local MCU connected to the Stem I2C.


### Supervisor access

The Supervisor can use the Stem I2C to change the boot for the SoM via Expanders. 
It has SDIO(SD2) which can emulate an SD Card for an alternate boot.
It just needs SYS_RST_PMIC and ALT_BOOT pins to do this.

The ideal method will be to provide an image via USB 2.0 HID according to the Serial boot option.
This would require access to BOOT_SEL pins to trigger this mode on reset.

Booting the SoM from this fake flash can be used to upgrade Expander firmware or SoM eMMC.

UART can be used by SoM to access LoRa on the card via COEX pins linked with UART2.

The Supervisor can use the Stem I2C to change wake state of the SoM.



### Slot Pin Allocation

The Slot supports regular M.2 Socket 2(Key B) cards such as WWAN+GNSS and NVMe SSD.
Beware that SATA and SSIC not supported

The module is used for cards with specific features

- GNSS / GPS
- WWAN LoRa/LTE
- UIM
- AUDIO
- PCIe (1 lane)
- USB3.1
- BLE (via USB 2.0)
- WiFi (via USB 2.0)
- WiFi (via PCIe)
- NVMe SSD (via PCIe)

Specifically,

- WWAN can make use of USB2.0, USB3.0, PCIe (single Lanes). The actual implemented I/F is identified through the Configuration pins state (2 options) on the Module side. LED1# and W_DISABLE1# are intended for use with the WWAN solution. There are additional WWAN and GNSS related pins including W_DISABLE2#, DPR, and WAKE_ON_WWAN#
- The UIM and SIM Detect pin are reserved for a future a SIM device on faceboard.
- The COEX, SIM DETECT, SUSCLK and ANTCTL are reserved for use by the Supervisor Card.
- An UART connection is reserved on COEX for LoRa/Debug/MCU
- The GPIO0..11 pins are allocated (Conf 1) to GNSS, AUDIO(SAI3), LED_1(SAI3), GPIO_10, and WAKE_ON_WWAN.
- The FULL_CARD_POWER_OFF# and the RESET# pins are unique and intended to be used when the WWAN solution is plugged into platforms that provide a direct connection to VBATT (and not a regulated 3.3 V) such as Tablet platforms. They are not used in NB and Very thin notebooks type platforms that provide a regulated 3.3 V power rail. But the FULL_CARD_POWER_OFF# signals should be tied to the 3.3 V power rail on the NB/very thin platform.
- The SSD can make use of the PCIe single lane. The actual implemented I/F is identified through the CONFIG_1 pin state (1 or 0) in conjunction with the other three Configuration pin states that are all 0. 
- The SUSCLK may be provided in future, and is used for SD2_CLK by Supervisor card.
- Input/Output of I2S is provided by mapping to SAI3 on the i.MX SoM. Note that separate L/R clock pins are used with a common bit clock.
- USB 3.1 RX/TX is allocated
- A one lane PCIe is allocated

The USB is connected to T-USB (not the M.2 expansions) on boot to support NVMe SSD expansions by default.
The USB data signals from SoM are multiplexed between T-USB Host (USB2) and M.2 Key B based on MUX_USB2_SEL & MUX_USB3_SEL.

According to documentation: Type refers to the signal direction:
• Type O means signal is an output from the MPU/MCU to the adapter. 
• Type I means signals is an input to the MPU/MCU from the adapter.


#### Control pins mapped by I/O Expander

The system I/O expander controls mPCIe_PERST which resets PCIe.
PCIE_CLKREQ_B is a direct pin on the SoM.
PCIE_WAKE_B is a direct pin on the SoM. 




### Key B pinouts

:[Key B pinouts](../pinouts/M2_KEY_B_CONNECTOR.md)


### Reference designs

:[M.2 Key B References](../refs/m.2/M2_KEY_B_REFS.md)


### Future directions

The Supervisor could provide a Linux Rootfs via USB mass storage interface.
The equivalent of [Wifi JTAG can be added](https://github.com/emard/wifi_jtag)

UART 2/4 for debug?

COEX pins may be used for SPI lines in the future.

TODO mapping I2S DIN/DOUT
