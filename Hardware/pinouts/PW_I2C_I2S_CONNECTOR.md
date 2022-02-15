Breaking out individual I2C/I2S busses adds common power. This is used for SCCB, Sound out and Sound in.

SCCB connector for Left/Right Camera modules.

| No. | Pin   | Description                  |
|-----|-------|------------------------------|
|  1  |	1V8   | Power at signal level 1.8V   |
|  2  |	GND   |	GND 	                     |
|  3  |	INT   | I2C Interrupt                |
|  4  | SCL   | I2C SCL                      | 
|  5  | SDA   | I2C SDA                      | 
|  6  |	5V    | Board power 5V               |

Speaker / Microphone connector

| No. | Pin         | Description                         |
|-----|-------------|-------------------------------------|
|  1  |	1V8 / 3V3   | Power at signal level 1.8V / 3.3V   |
|  2  |	GND   |	   GND 	                          |
|  3  |	BCLK  | I2S BCLK  / SAI5_TXC / SAI5_RXC	          |
|  4  | LRCLK | I2S LRCLK / SAI5_TXFS / SAI5_RXFS               | 
|  5  | DATA  | I2S DATA  / SAI5_TX0 / SAI5_RX0                | 
|  6  |	5V    | Board power 5V   |

Max. Current per pin 1.0A
