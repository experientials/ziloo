
Pin 1 is indicated on the board by a dot.

Toward thin part with microphone and other sensors

| Pin | Code       | Type     | Details                              | Voltage |
|-----|------------|----------|--------------------------------------|---------|
| 1   | AF_VDD     | Power    | Reserved for Autofocus               | 3.3V |
| 2   | AVDD_2V8   | Power    | Analog, Max 500mA                    | 2.8V |
| 3   | DOVDD      | Power    | Power for I/O circuit, Max 500mA     | 1.8V |
| 4   | VCC_1V8    | Power    | 1.8V ,MAX 200mA                      | 1.8V |
| 5   | GND        | Power    | GND                                  |      |
| 6   | CAM_FSIN   | I/O      | Frame sync input                     |      |
| 7   | CAM_STROBE | I/O      | Frame sync output                    |      |
| 8   | EXTCLK     | Input    | External Clock Input (MCLK)          |      |
| 9   | ATT_INT    | Output   | Interrupt Attached Sensor, Active L  | 1.8V? |
| 10  | ATT_XSHUT  | Input    | Attached Sensor XSHUTDOWN            | 1.8V |
| 11  | Reserved   | AF/PWM   | PWM Motor control (NC)               |      |
| 12  | I2C_SCL    | I/O      | I2C1_SCL(pullup resistor 2.2K)       | 1.8V |       
| 13  | I2C_SDA    | I/O      | I2C1_SDA(pullup resistor 2.2K)       | 1.8V |        
| 14  | BCLK / SCK | I2S      | Bit clock line                       | 1.8V |
| 15  | WS / LRCLK | I2S      | Word clock line                      | 1.8V |
| 16  | SDATA1     | I2S      | Input data 1                         | 1.8V |
| 17  | SDATA2     | I2S      | Input data 2 (NC)                    | 1.8V |


Towards image sensors

| Pin | Code       | Type     | Details                              | Voltage |
|-----|------------|----------|--------------------------------------|---------|
| 34  | AGND       |  Power   | Analog ground                        |         |
| 33  | RESET      | Input    | Camera Reset, Active Low (RSTB)      |         |
| 32  | PWRDN      | Input    | Camera Power Down                    |         |
| 31  | Reserved   |          |                                      |         |
| 30  | Reserved   |          |                                      |         |
| 29  | -          |          | GND                                  |         |
| 28  | CSI_RX_D0P | Camera   | MIPI_CSI_RX_D0+                      | 1.8V    |
| 27  | CSI_RX_D0N | Camera   | MIPI_CSI_RX_D0-                      | 1.8V    |
| 26  | -          |          | GND                                  |         |
| 25  | CSI_RX_D1P | Camera   | MIPI_CSI_RX_D1+                      | 1.8V    |
| 24  | CSI_RX_D1N | Camera   | MIPI_CSI_RX_D1-                      | 1.8V    |
| 23  | -          |          | GND                                  |         |
| 22  | CSI_RX_D2P | Camera   | MIPI_CSI_RX_D2+                      | 1.8V    |
| 21  | CSI_RX_D2N | Camera   | MIPI_CSI_RX_D2-                      | 1.8V    |
| 20  | -          |          | GND                                  |         |
| 19  | CSI_RX_CLKP| Camera   | MIPI_CSI_RX_CLK+                     | 1.8V    |
| 18  | CSI_RX_CLKN| Camera   | MIPI_CSI_RX_CLK-                     | 1.8V    |

