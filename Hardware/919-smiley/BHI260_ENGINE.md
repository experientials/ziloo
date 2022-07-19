The BOSCH sensor includes an embedded processor communicating via I2C. It boots from a 1MB flash chip. It runs and communicates on is 1.8V.

https://www.mouser.ch/ProductDetail/Bosch-Sensortec/BHI260AP?qs=T94vaHKWudTEPTnGI%252BTy9w%3D%3D

BHI260AB I2C modes support 3.4 Mbit/s. Put on SYS or 3 ? HSCX + HSDX. i.MX 8 can only do 400KHz.

Power comes from any of the SOM lines via the two 50 pins connectors. Isolate them and down regulate to 3.3V.

Host I2C is I2C3 on the CPU side.
Master I2C 2 is I2C6 on the CPU side, Right CAM CSI2 SCCB & Ambient Light.
Master I2C 3 is I2C5 on the CPU side, Left CAM CSI1 SCCB & Laser Scan.
Master is is free for SPI communication.

Sensor linux driver source - https://github.com/BoschSensortec/BHY2-Sensor-API

:[BHI260 pins](./BHI260_PINS.md)

Address

HSDO is LSB selecting 0x28 or 0x29 = LOW by default (can be overridden)

### QSPI Flash

Soldering Pads are reserved on the board for a 1MByte flash chip connected vis QSPI to the Bosch SensorTech

* CLK
* CSN
* D0..D3

It supports,
* Quad SPI / QPI modes
* 0.5 - 8 MBytes supported

I assume the voltage is 1.8V. Winbond is apparently a tested example.



