
| Pin | Code       | Description                              | 
|-----|------------|------------------------------------------|
|  1  | 3V3        |                                          |
|  2  | AUX+       | OTG alt AUX+ (SBU2)                     |
|  3  | AUX-       | OTG alt AUX- (SBU1)                     |
|  4  | 3V3        |                                          |
|  5  | OA+        | OTG A+                     |
|  6  | OA-        | OTG A-                     |
|  7  | 3V3        |                                          |
|  8  | OB+        | OTG B+                     |
|  9  | HB-        | OTG B-                     |
| 10  | 3V3        |                                          |
| 11  | OC+        | OTG C+                     |
| 12  | OC-        | OTG C-                     |
| 13  | 3V3        |                                          |
| 14  | OD+        | OTG D+                     |
| 15  | OD-        | OTG D-                     |
| 16  | GND        |                                          |
| 17  | OSBU1      | OTG alt SBU1                     |
| 18  | OSBU2      | OTG alt SBU2                     |
| 19  | GND        |                     |
| 20  | OX+        | OTG Extra 2.0 D+                     |
| 21  | OX-        | OTG Extra 2.0 D-                     |
| 22  | GND        |                                          |
| 23  | TRCLK+     | ETH0 TR CLK+                      |
| 24  | TRCLK-     | ETH0 TR CLK-                      |
| 25  | GND        |                     |
| 26  | TR1+      | ETH0 TR 1+                      |
| 27  | TR1-      | ETH0 TR 1-                      |
| 28  | GND        |                     |
| 29  | TR2+      | ETH0 TR 2+                      |
| 30  | TR2-      | ETH0 TR 2-                      |
| 31  | GND        |                     |
| 32  | TR3+      | ETH0 TR 3+                      |
| 33  | TR3-      | ETH0 TR 3-                      |
| 34  | GND        |                     |
| 35  | TR4+      | ETH0 TR 4+                      |
| 36  | TR4-      | ETH0 TR 4-                      |
| 37  | GND        |                     |
| 38  | I2C6 SCL   | LVDS TOUCH SCL                      |
| 39  | I2C6 SDA   | LVDS TOUCH SDA                      |
| 40  | TOUCH_INT  | LVDS TOUCH INT                    |
| 41  | TOUCH_RST  | LVDS TOUCH Reset                    |

SYS I2C
UART2 RXD TXD

TODO wiring up the extra enable/gpio pins
     wiring up the master I2C and others
    which lines LVDS are needed for conversion chip
    alt layout on Key E
     
Multiplexing status light lines I2C expander to expander
- LED_ACT
- LED_ETH 10_100
- LED_ETH 1000
- boot state
- PD Controller GPIO
