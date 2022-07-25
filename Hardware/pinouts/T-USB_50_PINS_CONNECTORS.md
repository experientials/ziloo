Two connectors tie the daughterboard to the bridge board. Both are of a 50 pin Highrose B2B type.

- [JLCPCB plug](https://jlcpcb.com/parts/componentSearch?isSearch=true&searchTxt=DF40C-50DP-0.4V)
- [JLCPCB socket](https://jlcpcb.com/parts/componentSearch?isSearch=true&searchTxt=DF40C-50DS-0.4V)

default height 1.5mm

Connector 1: High Speed Data
Connector 2: PD Controller, Debug, USB 2.0

| Power   |  Max Current | Pins |
|---------|--------------|------|
| VSOM    | 3.0 A        | 10   |
| GND     | 3.0 A        | 10   |
| VCC_RTC | 600 mA       | 2    |
| VIN_3V3 | 300 mA       | 1    |
| VIN_5V  | 600 mA       | 2    |
| LDO_3V3 | 300 mA       | 1    |


#### Connector 1 high-speed data, close to Alt Mode Breakout connectors

- 6 * GND
- 7 * VSOM

One side

| Pin | Code             | Type     | Details                              | Voltage | Misc         | MCU pin. |
|-----|------------------|----------|--------------------------------------|---------|--------------|----------|
| 1   | VSOM             | Power    | Main power for board 3.45V - 4.5V    |         | Conn. detect |          |
| 2   | USB1_RX_DP       | USB      | USB1 RX D+ (OTG)                     |         |              | HD3SS460 SSRX     |
| 3   | USB1_RX_DN       | USB      | USB1 RX D- (OTG)                     |         |              | HD3SS460 SSRX     |
| 4   | GND              | Power    | Ground                               |         |              |          |
| 5   | USB1_TX_DP       | USB      | USB1 TX D+ (OTG)                     |         |              | HD3SS460 SSTX     |
| 6   | USB1_TX_DN       | USB      | USB1 TX D- (OTG)                     |         |              | HD3SS460 SSTX         |
| 7   | GND              | Power    | Ground                               |         |              |          |
| 8   | USB2_RX_DP       | USB      | USB2 RX D+  (Host)                   |         |              | HD3SS460 SSRX         |
| 9   | USB2_RX_DN       | USB      | USB2 RX D-  (Host)                   |         |              | HD3SS460 SSRX         |
| 10  | GND              | Power    | Ground                               |         |              |          |
| 11  | USB2_TX_DP       | USB      | USB2 TX D+  (Host)                   |         |              | HD3SS460 SSTX         |
| 12  | USB2_TX_DN       | USB      | USB2 TX D-  (Host)                   |         |              | HD3SS460 SSTX         |
| 13  | GND              | Power    | Ground                               |         |              |          |
|     |                  |          |                                      |         |              |             | 
| 17  | STEM SCL         | I2C      | STEM SCL                             |         |              | GP21 I2C0   |
| 18  | STEM SDA         | I2C      | STEM SDA                             |         |              | GP20 I2C0   |
| 19  | STEM INT         | I2C      | Sensor interrupts                    |         |              |          |
| 20  | GND              | Power    | Ground                               |         |              |          |
| 21  | SWD CLK RP       | RP2040   |                                      |         |              |          |
| 22  | RUN_RP#          | RP2040   | Pull low to power off/reset RP       |         |              |             | 
| 23  | SWD DAT RP       | RP2040   |                                      |         |              |          |
| 24  | PWR_CHARGE       | Battery  | Internal charge current for testing  |         |              |          |
| 25  | BAT_STAT         | Battery  | Internal charging status for testing |         |              |          |



Other side

| Pin | Code       | Type     | Details                              | Voltage | Misc         | MCU pin. |
|-----|------------|----------|--------------------------------------|---------|--------------|----------|
| 50  | LVCLK+     | LVDS     | LVDS CLK+                            |         |              |          |
| 49  | LVCLK-     | LVDS     | LVDS CLK-                            |         |              |          |
| 48  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |              |          |
| 47  | LVD0+      | LVDS     | LVDS D0+                             |         |              |          |
| 46  | LVD0-      | LVDS     | LVDS D0-                             |         |              |          |
| 45  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |              |          |
| 44  | LVD1+      | LVDS     | LVDS D1+                             |         |              |          |
| 43  | LVD1-      | LVDS     | LVDS D1-                             |         |              |          |
| 42  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |              |          |
| 41  | LVD2+      | LVDS     | LVDS D2+                             |         |              |          |
| 40  | LVD2-      | LVDS     | LVDS D2-                             |         |              |          |
| 39  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |              |          |
| 38  | LVD3+      | LVDS     | LVDS D3+                             |         |              |          |
| 37  | LVD3-      | LVDS     | LVDS D3-                             |         |              |          |
| 36  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |              |          |
| 35  |            |          |                                      |         |              |          |
| 34  |            |          |                                      |         |              |          |
| 33  | GND        | Power    | Ground                               |         |              |          |
| 32  | CAN_RX     |          | CAN1_RX                              |         | P21.12       |          |
| 31  | CAN_TX     |          | CAN1_TX                              |         | P21.14       |          |
| 30  | BAT_LDO    | Battery  | 4.9V 50mA LDO for STAT LED           |         |              |          |
| 29  | BOOTSEL_RP | RP2040   | Boot Mode Select for RP              |         |              |          |
| 28  | UART_RP_TXD| Debug    |                                      |         |              | GP0      |
| 27  | UART_RP_RXD| Debug    |                                      |         |              | GP1      |
| 26  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |              |          |

Could also take in HDMI or PCIe lanes instead of LVDS


#### Connector 2 PD controller, close to power connectors

- 2 * VSOM, 3 * GND, 1 * VCC_RTC, 1 * VIN_3V3
- 1 * VSOM, 1 * GND, 2 * VIN_5V

One side

| Pin | Code         | Type     | Details                              | Voltage | Misc         |
|-----|--------------|----------|--------------------------------------|---------|--------------|
| 1   | VSOM         | Power    | Main power for board 3.45V - 4.5V    |         | Conn. detect |
| 2   | GND          | Power    | Ground                               |         |              |
| 3   | USB1_DP      | USB      | USB1 D+                              |         |              |
| 4   | USB1_DN      | USB      | USB1 D-                              |         |              |
| 5   | GND          | Power    | Ground                               |         |              |
| 6   | USB2_DP      | USB      | USB2 D+                              |         |              |
| 7   | USB2_DN      | USB      | USB2 D-                              |         |              |
| 8   | GND          | Power    | Ground                               |         |              |
| 9   | PD_SWD_CLK   | Debug    | PD Controller GPIO12                 |         |              |
| 10  | PD_SWD_DAT   | Debug    | PD Controller GPIO13                 |         |              |
| 11  | BOTH_VSOM    | Enable   | Bridge board signal;VSOM connected on both sides |         |   |
| 12  | MCU_SYS_INT  | IRQ      | When state of MCUs change -> SoM     |         | EX0.2 |             |
| 13  | SYS I2C SCL  | I2C      |                                      |         | P21.7        | GP15 I2C1.  |
| 14  | SYS I2C SDA  | I2C      |                                      |         | P21.5        | GP14 I2C1.  |
| 15  | VSOM_LOCK    | Power    | Main power for board 3.45V - 4.5V, if mechanical lock shorted    |         | Mech. lock |
| 16  | SYS_RST_PMIC | Reset    | PMIC reset input pin. Internally pulled up with LDO1 power rail. Once low, PMIC performs reset. |         | P10.9   |
| 17  | POR_B_3P3    | Reset    | Power On reset output pin. Open drain output requiring external pull up resistor. |    | P10.7 |
| 18  | PMIC_ON_REQ  | Reset    | PMIC ON input from Application processor. When high, the device starts power on sequence. |     | P10.5   |
| 19  | PMIC_STBY_REQ| Reset    | Standby mode input from Application processor. When high, device enters STANDBY mode. |     | P10.3  |
| 20  | VCC_RTC      | Power    | Low power mode supply                |         |   |
| 21  | PWRBTN       | Boot     | Power button trigger                 |         |   |
| 22  | ALT_BOOT     | Boot     | Alternate boot                       |         |   |
| 23  | QSPI_BOOT_EN_3P3| Boot  | SPI boot                             |         |  P21.18   |
| 24  | BAT_CE#      | Charger  | Charge Enable Active-Low. Connect CE to a high logic level to place the battery charger in standby mode.  |      |    |
| 25  | PD_VIN_EN    | Future   | Enable VIN_5V/3V3 from PWR_SYS (TBD) |         |    |

Other side

| Pin | Code       | Type     | Details                              | Voltage |  Misc   | mcu pin |
|-----|------------|----------|--------------------------------------|---------|---------|---------|
| 50  | PD_HRESET  | Future   | PD Controller HRESET (High)          |         |         |         |
| 49  | GND        | Power    | Ground                               |         |         |         |
| 48  | UART1_TXD  | UART     | P1.72 UART1 Tx                       |         | P20.9   | GP4 UART1    |
| 47  | UART1_RXD  | UART     | P1.19 UART1 Rx                       |         | P20.11  | GP5 UART1    |
| 46  | UART2_TXD  | UART     | UART2 Tx                             |         | P20.1   | GP8 UART1.   |
| 45  | UART2_RXD  | UART     | UART2 Rx                             |         | P20.3   | GP9 UART1    |
| 44  | UART3_TXD  | UART     | P1.61 UART3 Tx                       |         | P20.2   | GP12 UART0   |
| 43  | UART3_RXD  | UART     | P1.21 UART3 Rx                       |         | P20.4   | GP13 UART0   |
| 42  | UART4_TXD  | UART     | UART4 Tx                             |         | P20.8   | GP20 UART1 |
| 41  | UART4_RXD  | UART     | UART4 Rx                             |         | P20.10  | GP21 UART1 |
| 40  | MIC_CLK    | Sensor   | frontboard mic                       |         |         |    |
| 39  | MIC_DATA   | Sensor   |                                      |         |         |    |
| 38  | MIC_INT    | Sensor   |                                      |         |  ?      |    |
| 37  | MOTION_INT | Sensor   | frontboard motion mic on stem I2C    |         |  ?      |    |
| 36  | NIGHT SCL  | I2C      | I2C6 SCL                             |         | P21.2   | GP19 I2C1.   |
| 35  | NIGHT SDA  | I2C      | I2C6 SDA                             |         | P21.4   | GP18 I2C1.   |
| 34  | NIGHT INT  | I2C      | Sensor interrupts                    |         |         |         |
| 33  | SPI_CS     | RP2040   | RP SPI                               | 3.3V    |         | GP29 SPI1 |
| 32  | SPI_CLK    | RP2040   | RP SPI                               | 3.3V    |         | GP10 SPI |
| 31  | SPI_MISO   | RP2040   | RP SPI                               | 3.3V    |         | GP28 SPI |
| 30  | SPI_MOSI   | RP2040   | RP SPI                               | 3.3V    |         | GP11 SPI |
| 29  | VIN_3V3    |          | Supply for TPS64988 circuitry and I/O. Current 50 mA |   3.3V        |     |    |
| 28  | VIN_5V     | Power    | System 5V power source (PPHV1, PPHV2, PP1_CABLE, PP2_CABLE). 500 mA. | 5V      |    |     |
| 27  | VIN_5V     | Power    | System 5V power source (PPHV1, PPHV2, PP1_CABLE, PP2_CABLE). 500 mA. | 5V      |    |     |
| 26  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |  Conn. detect |     |

SPI pins will be exchanged for SDIO (MIC_INT / MOTION_INT / PD_HRESET likely to go away)

Consider SPI for PD Controller
PD Controller IRQ I2C1
