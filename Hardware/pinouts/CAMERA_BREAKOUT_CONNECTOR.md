
| Pin | Code       | Description                              | 
|-----|------------|------------------------------------------|
| 1   | CAM_FSIN  | Left Frame sync input                    |      
| 2   | CAM_STROBE| Left Frame sync output                   |      
| 3   | ATT_INT   | Left Interrupt Attached Sensor, Active L |
| 4   | ATT_XSHUT | Left Attached Sensor XSHUTDOWN           |
| 5   | AF_PWM   | PWM Motor control                        |      
| 6  | BCLK / SCK | Bit clock line                       | 
| 7  | WS / LRCLK | Word clock line                      | 
| 8  | SDATA1     | Input data 1                         | 

| 19  | PD_I2C1_SCL| I2C1_SCL(pullup resistor 2.2K)       | 
| 20  | PD_I2C1_SDA| I2C1_SDA(pullup resistor 2.2K)       | 
| 21  | PD_I2C2_SCL| I2C2_SCL(pullup resistor 2.2K)       | 
| 24  | PD_I2C2_SDA| I2C2_SDA(pullup resistor 2.2K)       | 
| 25  | GND        |                     |
| 26  | GND        |                     |


Split in 2 for each camera side (8 pins + V_DATA/GND)

Or single row of holes in the sides (Samtec PHT   PHT-110-01-S-S (CAD))

PD Controller breakout in middle 4 * I2C + VIN/5V/GND