### DF40 60 pin connector

- SYS I2C
- I2C3
- ETH0
- LVDS
- HDMI
- UART2 / UART4
- USB1 2.0 / 3.1 pairs
- USB2 2.0 / 3.1 pairs
- GND
- 3V3 / 3V7 / 2V8
- 5V


EXTRA height ?

default height 1.5mm


| Pin | Code         | Type     | Details                              | Voltage |
|-----|--------------|----------|--------------------------------------|---------|
| 1   | VSOM         | Power    | Main power for board 3.45V - 4.5V    |         |
| 2   | GND          | Power    | Ground                               |         |
| 3   | USB1_DP      | USB      | USB1 D+                              |         |
| 4   | USB1_DN      | USB      | USB1 D-                              |         |
| 5   | USB1_RX_DP   | USB      | USB1 RX D+                           |         |
| 6   | USB1_RX_DN   | USB      | USB1 RX D-                           |         |
| 7   | GND          | Power    | Ground                               |         |
| 8   | USB1_TX_DP   | USB      | USB1 TX D+                           |         |
| 9   | USB1_TX_DN   | USB      | USB1 TX D-                           |         |
| 10  | GND          | Power    | Ground                               |         |
| 11  | VSOM         | Power    | Main power for board 3.45V - 4.5V    |         |
| 12  | SYS_nINT     | IRQ      | Interrupt signal (GPIO4_IO19)        |      |
| 13  | EX_OH_nINT   | IRQ      | Interrupt signal (GPIO1_IO0)         |      |
| 14  | STEM_T_nINT  | IRQ      | Interrupt signal (GPIO1_IO1).        |      |
| 15  | VSOM         | Power    | Main power for board 3.45V - 4.5V    |         |
| 16  | SYS_RST_PMIC | Reset    | PMIC reset input pin. Internally pulled up with LDO1 power rail. Once low, PMIC performs reset. |         |
| 17  | POR_B_3P3    | Reset    | Power On reset output pin. Open drain output requiring external pull up resistor. |    |
| 18  | PMIC_ON_REQ  | Reset    | PMIC ON input from Application processor. When high, the device starts power on sequence. |     |
| 19  | PMIC_STBY_REQ| Reset    | Standby mode input from Application processor. When high, device enters STANDBY mode. |     |
| 20  | VSOM         | Power    | Main power for board 3.45V - 4.5V    |         |
| 21  | VCC_RTC      | Power    | Low power mode supply                |         |
| 22  | GND          | Power    | Ground                               |         |
| 23  | PWRBTN       | Boot     | Power button trigger                 |         |
| 24  | ALT_BOOT     | Boot     | Alternate boot                       |         |
| 25  |QSPI_BOOT_EN_3P3| Boot   | SPI boot                             |         |
| 26  |              | Reserved |                                      |         |
| 27  |              | Reserved |                                      |         |
| 28  | GND          | Power    | Ground                               |         |
| 29  |              | Reserved |                                      |         |
| 30  | VSOM         | Power    | Main power for board 3.45V - 4.5V    |         |





| Pin | Code       | Type     | Details                              | Voltage |
|-----|------------|----------|--------------------------------------|---------|
| 60  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |
| 59  | GND        | Power    | Ground                               |         |
| 58  | USB2_DP    | USB      | USB2 D+                              |         |
| 57  | USB2_DN    | USB      | USB2 D-                              |         |
| 56  | USB2_RX_DP | USB      | USB2 RX D+                           |         |
| 55  | USB2_RX_DN | USB      | USB2 RX D-                           |         |
| 54  | GND        | Power    | Ground                               |         |
| 53  | UART1_TXD  | UART     | P1.72 UART1 Tx                       |         |
| 52  | UART1_RXD  | UART     | P1.19 UART1 Rx                       |         |
| 51  | GND        | Power    | Ground                               |         |
| 50  | UART2_TXD  | UART     | UART2 Tx                             |         |
| 49  | UART2_RXD  | UART     | UART2 Rx                             |         |
| 48  | UART3_TXD  | UART     | P1.61 UART3 Tx                       |         |
| 47  | UART3_RXD  | UART     | P1.21 UART3 Rx                       |         |
| 46  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |
| 45  | UART4_TXD  | UART     | UART4 Tx                             |         |
| 44  | UART4_RXD  | UART     | UART4 Rx                             |         |
| 43  | GND        | Power    | Ground                               |         |
| 42  | I2C SCL    | I2C      | P1.99 SYS SCL                        |         |
| 41  | I2C SDA    | I2C      | P1.97 SYS SDA                        |         |
| 40  | VCC_RTC    | Power    | Low power mode supply                |         |
| 39  | I2C3 SCL   | I2C      | Stem SCL                             |         |
| 38  | I2C3 SDA   | I2C      | Stem SDA                             |         |
| 37  | GND        | Power    | Ground                               |         |
| 36  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |
| 35  |            | Reserved |                                      |         |
| 34  |            | Reserved |                                      |         |
| 33  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |
| 32  | VSOM       | Power    | Main power for board 3.45V - 4.5V    |         |



