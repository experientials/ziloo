![Back GPIO header](../pinouts/back-face-gpio.png)

| Left side                  | Function  |Pin |Pin | Function  | Right side           |
|----------------------------|-----------|----|----|-----------|----------------------|
|  When VSOM fully connected | 3V3_ON    | 1  | 2  | VCC_FULL  | When VSOM fully connected  |
|       I2C3 SDA / STEM_SDA  | SDA       | 3  | 4  | VCC_FULL  | When VSOM fully connected |
|       I2C3 SCL / STEM_SCL  | SCL       | 5  | 6  | GND       |                      |
|                   STEM_INT | INT       | 7  | 8  | TxD       | UART2 TxD            |
|                            | GND       | 9  | 10 | RxD       | UART2 RxD            |
|                            |           | 11 | 12 | SWD       | SWDCLK for T-USB     |
|     SDIO DAT3 / GPIO2_IO18 | SDIO      | 13 | 14 | SWD       | SWDIO for T-USB      |
|      SDIO CLK / GPIO2_IO13 | SDIO      | 15 | 16 | SDIO      | SDIO CMD / GPIO2_IO14  |
|    When any VSOM connected | 3V3       | 17 | 18 | SDIO      | SDIO DAT0 / GPIO2_IO15 |
| ECSPI2_MOSI / GPIO5_IO11   | MOSI      | 19 | 20 | GND       |                        |
| ECSPI2_MISO / GPIO5_IO12   | MISO      | 21 | 22 | SDIO      | SDIO DAT1 / GPIO2_IO16 |
| ECSPI2_SCLK / GPIO5_IO10   | SCLK      | 23 | 24 | SPI CE0   | ECSPI2_SS0/GPIO5_IO13  |
|                            | GND       | 25 | 26 | SCL       | NIGHT SCL            |
|                    SYS I2C | SYS SDA   | 27 | 28 | SCL       | SYS I2C              |
|                  NIGHT_INT | INT       | 29 | 30 | (GND)     |                      |
|                  NIGHT_SDA | SDA       | 31 | 32 | TxD       | UART4 TX             |
|                   UART4 RX | RxD       | 33 | 34 | JTAG      | SoM JTAG CLK (RPi GND) |
|    Battery measuring point | BAT_LDO   | 35 | 36 | JTAG      | SoM JTAG DIO          |
|     SDIO DAT2 / GPIO2_IO17 | SDIO      | 37 | 38 | CAN2      | CAN2 RX / GPIO4_IO27  |
|               (GND on RPi) |           | 39 | 40 | CAN2      | CAN2 TX / GPIO4_IO26  |


