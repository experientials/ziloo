| Code   | All | T-USB       | Cam  | Probe     | Description                            | Function  | SoM Dev Board |
|--------|-----|-------------|------|-----------|------------------------------------------|-----------|---------------|
| GP00   |     |             |      |           | UART_RP_TXD for debugging                | F2 UART0  | -             |
| GP01   |     |             |      |           | UART_RP_RXD for debugging                | F2 UART0  | -             |
| GP02   | x   |             |      |           | STEM INT Sensor / Expander IRQ           |           |            
| GP03   | x   |             |      |           | NIGHT INT Sensor IRQ                     |           |
| GP04   | x   |             |      |           | SYS I2C SDA                              | F3 I2C0   | P1.97         |
| GP05   | x   |             |      |           | SYS I2C SCL                              | F3 I2C0   | P1.99         | 
| GP06   |     | VM3011 CLK  |      | MSP_SBWTCK | Mapped to MSP430                                      | | |
| GP07   |     | VM3011 DATA |      | MSP_SBWTDIO |                                       | | |
| GP08   |     | UART1 Tx    |      | UART2 Tx  |                                          | F2 UART1  | P20.1   |
| GP09   |     | UART1 Rx    |      | UART2 Rx  |                                          | F2 UART1  | P20.3   |
| GP10   | x   |             |      | SDIO CLK  | SDIO CLK / SPI_CLK                       | F1 SPI1 | |
| GP11   | x   |             |      | SDIO CMD  | SDIO CMD / SPI_MOSI or TX                | F1 SPI1 | |
| GP12   |     | UART3 Tx    |      | UART4 Tx  |                    | F2 UART0  | P20.2 / P1.61 |
| GP13   |     | UART3 Rx    |      | UART4 Rx  |                   | F2 UART0  | P20.4 / P1.21 |
| GP14   | x   |             | DAT1 | SDIO DAT1 | SDIO DATA 1                              | F0 GPIO| |
| GP15   | x   |             | DAT2 | SDIO DAT2 | SDIO DATA 2                              | F0 GPIO| |
| GP16   |     |             | DAT0 | Probe UART TX |                                      | F3 I2C0   | -             | 
| GP17   |     |             | DAT4 | Probe UART RX |                                      | F3 I2C0   | -             | 
| GP18   | x   |             |      |           | Night I2C6 SDA                           | F3 I2C1   | P21.4         |
| GP19   | x   |             |      |           | Night I2C6 SCL                           | F3 I2C1   | P21.2         |
| GP20   | x   |             |      |           | STEM SDA                                 | F3 I2C0   | -             | 
| GP21   | x   |             |      |           | STEM SCL                                 | F3 I2C0   | -             | 
| GP22   | x   |             | DAT3 | SDIO DAT3 | SDIO DATA 3                              | F8 CLOCK GPIN1     |
| GP23   |     |             | MCLK |           | - Reserved for Speaker I2S SDO (Dev buck mode) | F8 CLOCK GPOUT1    |
| GP24   |     |             | VSYNC|           | - Reserved for Speaker I2S BCK (Dev VBUS voltage)          |      |   |
| GP25   |     |             | HREF |           | - Reserved for Speaker I2S LRCK (Dev LED)         |      |
| GP26   |     | x           |      | MSP_DTR   | Reserved Human Body analog signal        | Fx ADC  |
| GP27   |     | x           |      | MSP_RTS   | Reserved Voltage / Analog Sensor         | Fx ADC |
| GP28   | x   |             |      | SDIO DAT0 | SDIO DATA0 / SPI_MISO or RX              | F1 SPI1 |
| GP29   |     |             |      |          | SPI_CS, reserved, do not connect (Lipo Dev Voltage)        | F1 SPI1 |
| USB_DM |     | Stem USB D- |      | Probe D- | USB 2.0 D-                          |
| USB_DP |     | Stem USB D+ |      | Probe D+ | USB 2.0 D+                          | 
| USB_VDD|     |             |       | Not used                                 |


