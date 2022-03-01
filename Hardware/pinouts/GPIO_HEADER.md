
| Left side                  | Function  |Pin |Pin | Function  | Right side           |
|----------------------------|-----------|----|----|-----------|----------------------|
|                            | 3V3       | 1  | 2  | 5V        |                      |
|     I2C3_SDA / GPIO5_IO19  | SDA 3     | 3  | 4  | 5V        |                      |
|     I2C3_SCL / GPIO5_IO18  | SCL 3     | 5  | 6  | GND       |                      |
|  ETH0_MDI2P / SAI7_TX_SYNC | SAI7 SYNC | 7  | 8  | TxD       | UART1 TxD / GPIO5_IO23   |
|                            | GND       | 9  | 10 | RxD       | UART1 RxD / GPIO5_IO22   |
|     EX_OH_nINT / GPIO1_IO0 | GPIO1_IO0 | 11 | 12 | GPIO1_IO1  | GPIO1_01 / EX_T_nINT  |
|     EX0_nINT / GPIO4_IO19  | GPIO4_IO19| 13 | 14 | GPIO2_IO19|                      |
|                            | GPIO2_IO8 | 15 | 16 | GPIO4_IO16|                      |
|        Powering suspended  | VCC_RTC   | 17 | 18 | GPIO4_IO17|                      |
| ECSPI2_MOSI / GPIO5_IO11   | MOSI      | 19 | 20 | GND       |                      |
| ECSPI2_MISO / GPIO5_IO12   | MISO      | 21 | 22 | GPIO1_IO19| TD2                     |
| ECSPI2_MOSI / GPIO5_IO10   | SCLK      | 23 | 24 | SPI CE0   | ECSPI2_SS0 / GPIO5_IO13 |
|                            | GPIO2_IO9 | 25 | 26 | QSPI BOOT | QSPI_BOOT_EN_3P3 |
|                    SYS I2C | SYS SDA   | 27 | 28 | SYS SCL   | SYS I2C               |
|     UART3_TXD / GPIO5_IO27 | UART3_TXD | 29 | 30 | GPIO5_IO26| UART3_RXD / GPIO5_IO26 |
|                  GPIO5_IO4 | PWM2      | 31 | 32 | PWM3      | GPIO5_IO3             |
|                  GPIO5_IO5 | PWM1      | 33 | 34 | CAN1_RX   | GPIO4_IO25     (RPi GND)      |
|     UART2_RXD / GPIO5_IO24 | GPIO5_IO24| 35 | 36 | CAN1_TX   | GPIO4_IO22           |
|     UART2_TXD / GPIO5_IO25 | GPIO5_IO25| 37 | 38 | CAN2_RX   | GPIO4_IO27           |
|                            | GND       | 39 | 40 | CAN2_TX   | GPIO4_IO26            |

