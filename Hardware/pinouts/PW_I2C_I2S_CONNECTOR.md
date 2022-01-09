Breaking out individual I2C/I2S busses adds common power. This is used for SCCB, Sound out and Sound in.

| No. | Pin         | Description                         |
|-----|-------------|-------------------------------------|
|  1  |	1V8 / 3V3   | Power at signal level 1.8V / 3.3V   |
|  2  |	GND         |	   GND 	                          |
|  3  |	INT / BCLK  | I2C Interrupt / I2S BCLK	          |
|  7  | SCL / LRCLK |   I2C SCL                           | 
|  8  | SDA         | I2C SDA                             | 
|  4  |	5V          | Board power 5V   |

Max. Current per pin 1.0A
