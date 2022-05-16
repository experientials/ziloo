Two connectors tie the daughterboard to the bridge board. Both are of a 50 pin Highrose B2B type.

- [JLCPCB plug](https://jlcpcb.com/parts/componentSearch?isSearch=true&searchTxt=DF40C-50DP-0.4V)
- [JLCPCB socket](https://jlcpcb.com/parts/componentSearch?isSearch=true&searchTxt=DF40C-50DS-0.4V)

default height 1.5mm

Connector 1: High Speed Data
Connector 2: PD Controller, Debug, USB 2.0

| Power   |  Max Current | Pins |
|---------|--------------|------|
| VSOM    | 3.0 A        | 9    |
| GND     | 3.0 A        | 9    |
| VCC_RTC | 600 mA       | 2    |
| VIN_3V3 | 300 mA       | 1    |
| VIN_5V  | 600 mA       | 2    |
| LDO_3V3 | 300 mA       | 1    |


#### Connector 1 high-speed data, close to Alt Mode Breakout connectors

- 6 * GND
- 7 * VSOM

One side

| Pin | Code             | Type     | Details                              | Voltage | Misc         |
|-----|------------------|----------|--------------------------------------|---------|--------------|
| 1   | VSOM             | Power    | Main power for board 3.45V - 4.5V    |         | Conn. detect |
| 2   | USB1_RX_DP       | USB      | USB1 RX D+                           |         |
| 3   | USB1_RX_DN       | USB      | USB1 RX D-                           |         |
| 4   | GND              | Power    | Ground                               |         |
| 5   | USB1_TX_DP       | USB      | USB1 TX D+                           |         |
| 6   | USB1_TX_DN       | USB      | USB1 TX D-                           |         |
| 7   | GND              | Power    | Ground                               |         |
| 8   | USB1_RX_DP       | USB      | USB2 RX D+                           |         |
| 9   | USB1_RX_DN       | USB      | USB2 RX D-                           |         |
| 10  | GND              | Power    | Ground                               |         |
| 11  | USB1_TX_DP       | USB      | USB2 TX D+                           |         |
| 12  | USB1_TX_DN       | USB      | USB2 TX D-                           |         |
| 13  | GND              | Power    | Ground                               |         |
| 14  | T_USB_O_ALT_EN   | AltMode  | Exposed EX3                          |         |
| 15  | T_USB_O_ALT_POL  | AltMode  | Exposed EX3                          |         |
| 16  | T_USB_O_ALT_AMSEL| AltMode  | Exposed EX3                          |         |
| 17  | T_USB_H_ALT_EN   | AltMode  | Exposed EX3                          |         |
| 18  | T_USB_H_ALT_POL  | AltMode  | Exposed EX3                          |         |
| 19  | T_USB_H_ALT_AMSEL| AltMode  | Exposed EX3                          |         |
| 20  | GND              | Power    | Ground                               |         |
| 21  |                  |          |                                      |         |
| 23  |                  |          |                                      |         |
| 24  | PWR_CHARGE       | Battery  | Internal charge current for testing  |         |
| 25  | BAT_STAT         | Battery  | Internal charging status for testing |         |

<mark>TODO remove EX3 exposure</mark>


Other side

| Pin | Code       | Type     | Details                              | Voltage |
|-----|------------|----------|--------------------------------------|---------|
| 50  | LVCLK+     | LVDS     | LVDS CLK+                            |         |
| 49  | LVCLK-     | LVDS     | LVDS CLK-                            |         |
| 48  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |
| 47  | LVD0+      | LVDS     | LVDS D0+                             |         |
| 46  | LVD0-      | LVDS     | LVDS D0-                             |         |
| 45  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |
| 44  | LVD1+      | LVDS     | LVDS D1+                             |         |
| 43  | LVD1-      | LVDS     | LVDS D1-                             |         |
| 42  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |
| 41  | LVD2+      | LVDS     | LVDS D2+                             |         |
| 40  | LVD2-      | LVDS     | LVDS D2-                             |         |
| 39  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |
| 38  | LVD3+      | LVDS     | LVDS D3+                             |         |
| 37  | LVD3-      | LVDS     | LVDS D3-                             |         |
| 36  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |
| 35  |              |        |                                      |         |
| 34  |              |        |                                      |         |
| 20  | GND        | Power    | Ground                               |         |
| 32  |              |        |                                    |         |
| 31  |              |        |                                    |         |
| 30  | BAT_LDO      | Battery| 4.9V 50mA LDO for STAT LED         |         |
| 28  |              |        |                                    |         |
| 27  |              |        |                                    |         |
| 26  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |  Conn. detect |

Could also take in HDMI or PCIe lanes


#### Connector 2 PD controller, close to power connectors

- 2 * VSOM, 3 * GND, 1 * VCC_RTC, 1 * VIN_3V3
- 1 * VSOM, 1 * GND, 1 * VCC_RTC, 2 * VIN_5V, 1 * LDO_3V3

One side

| Pin | Code         | Type     | Details                              | Voltage | Misc    |
|-----|--------------|----------|--------------------------------------|---------|---------|
| 1   | VSOM         | Power    | Main power for board 3.45V - 4.5V    |         | Conn. detect |
| 2   | GND          | Power    | Ground                               |         |         |
| 3   | USB1_DP      | USB      | USB1 D+                              |         |         |
| 4   | USB1_DN      | USB      | USB1 D-                              |         |         |
| 5   | GND          | Power    | Ground                               |         |         |
| 6   | USB2_DP      | USB      | USB2 D+                              |         |         |
| 7   | USB2_DN      | USB      | USB2 D-                              |         |         |
| 8   | GND          | Power    | Ground                               |         |         |
| 9   | SWD_CLK      | Debug    | PD Controller GPIO12                 |         |         |
| 10  | SWD_DAT      | Debug    | PD Controller GPIO13                 |         |         |
| 11  | BOTH_VSOM    | Enable   | Signal from bridge board that VSOM is connected on both sides   |         |   |
| 12  | EX0_nINT     | IRQ      | Interrupt signal (GPIO4_IO19)        |         | P21.30  |
| 13  | EX_OH_nINT   | IRQ      | Interrupt signal (GPIO1_IO0)         |         | P20.12  |
| 14  | EX_T_nINT    | IRQ      | Interrupt signal (GPIO1_IO1).        |         | P20.14  |
| 15  | VSOM_LOCK    | Power    | Main power for board 3.45V - 4.5V, if mechanical lock shorted    |         | Mech. lock |
| 16  | SYS_RST_PMIC | Reset    | PMIC reset input pin. Internally pulled up with LDO1 power rail. Once low, PMIC performs reset. |         | P10.9   |
| 17  | POR_B_3P3    | Reset    | Power On reset output pin. Open drain output requiring external pull up resistor. |    | P10.7 |
| 18  | PMIC_ON_REQ  | Reset    | PMIC ON input from Application processor. When high, the device starts power on sequence. |     | P10.5   |
| 19  | PMIC_STBY_REQ| Reset    | Standby mode input from Application processor. When high, device enters STANDBY mode. |     | P10.3  |
| 20  | VCC_RTC      | Power    | Low power mode supply                |         |   |
| 21  | PWRBTN       | Boot     | Power button trigger                 |         |   |
| 22  | ALT_BOOT     | Boot     | Alternate boot                       |         |   |
| 23  | QSPI_BOOT_EN_3P3| Boot  | SPI boot                             |         |  P21.18   |
| 24  | BAT_CE#      | Charger  |  Charge Enable Active-Low Input. Connect CE to a high logic level to place the battery charger in standby mode.  |         |    |
| 25  | PD_VIN_EN    |          | Enable VIN_5V/3V3 from PWR_SYS (TBD) |         |    |

Other side

| Pin | Code       | Type     | Details                              | Voltage |  Misc    |
|-----|------------|----------|--------------------------------------|---------|---------|
| 50  | RESERVED   |          | No Connect                           |         |         |
| 49  | GND        | Power    | Ground                               |         |
| 48  | UART1_TXD  | UART     | P1.72 UART1 Tx                       |         | P20.9   |
| 47  | UART1_RXD  | UART     | P1.19 UART1 Rx                       |         | P20.11  |
| 46  | UART2_TXD  | UART     | UART2 Tx                             |         | P20.1   |
| 45  | UART2_RXD  | UART     | UART2 Rx                             |         | P20.3   |
| 44  | UART3_TXD  | UART     | P1.61 UART3 Tx                       |         | P20.2   |
| 43  | UART3_RXD  | UART     | P1.21 UART3 Rx                       |         | P20.4   |
| 42  | UART4_TXD  | UART     | UART4 Tx                             |         | P20.8   |
| 41  | UART4_RXD  | UART     | UART4 Rx                             |         | P20.10  |
| 40  | I2C SCL    | I2C      | P1.99 SYS SCL                        |         | P21.7   |
| 39  | I2C SDA    | I2C      | P1.97 SYS SDA                        |         | P21.5   |
| 38  | I2C3 SCL   | I2C      | Stem SCL                             |         | P21.2 ? |
| 37  | I2C3 SDA   | I2C      | Stem SDA                             |         | P21.4 ? |
| 36  | VCC_RTC    | Power    | Low power mode supply                |         | |
| 35  | LDO_3V3    | Power    | Supply for SPI Flash. Current 50 mA  | 3.3V    |  |
| 34  | SPI_3V3    | Power    | Power to the flash chip. Bridge connects to VIN_3V3      | 3.3V    |
| 33  | SPI_CS     | PD     | Programming/External flash directly  | 3.3V    |
| 32  | SPI_CLK    | PD     | Programming/External flash directly  | 3.3V    |
| 31  | SPI_MISO   | PD     | Programming/External flash directly  | 3.3V    |
| 30  | SPI_MOSI   | PD     | Programming/External flash directly  | 3.3V    |
| 29  | VIN_3V3    |          | Supply for TPS64988 circuitry and I/O. Current 50 mA |   3.3V        |
| 28  | VIN_5V     | Power    | System 5V power source (PPHV1, PPHV2, PP1_CABLE, PP2_CABLE). 500 mA. | 5V      |
| 27  | VIN_5V     | Power    | System 5V power source (PPHV1, PPHV2, PP1_CABLE, PP2_CABLE). 500 mA. | 5V      |
| 26  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |  Conn. detect |

