# 919 Smiley

Face board used to face the user and bridge daughterboards.

It contains a Bosch Sensortech 32 bit RISC processor that monitors 3D movement using a gyroscope and accelerometer.
It communicates with the Host MCU via the Stem I2C bus (I2C3 for the MCU daughterboard). 
It exposes system control signals via the SYS I2C GPIO Expander 0.
Sensors on camera modules are available via Master 2 & 3.

A second chip is optional BMM150 to provide a magnetometer.


Alternate battery connection option for running detached.

Breakouts
- BATT in
- JTAG
- Master 1 SPI + 4 chip selects
- GPIOs : M2SDI


Components

- [Bosch Sensortech BHI260AP](https://www.bosch-sensortec.com/products/smart-sensors/bhi260ap/) - [Mouser](https://www.mouser.ch/ProductDetail/Bosch-Sensortec/BHI260AP)
- [NOR Flash 8M QSPI IS25WP080D-JNLE ISSI SOIC-8]() - [Mouser](https://www.mouser.ch/ProductDetail/ISSI/IS25WP080D-JNLE?qs=pif5%252B9MYt0UdCheWbE26RA%3D%3D)
- [LP5036 36 LED driver](https://www.ti.com/product/LP5036?keyMatch=LP5036) - [Mouser](https://www.mouser.ch/ProductDetail/Texas-Instruments/LP5036RJVR)
- [Würth 710-150040RS73220 1mm x 0.5mm red](https://www.mouser.ch/ProductDetail/710-150040RS73220)
- [Würth 710-150040VS73220 1mm x 0.5mm green](https://www.mouser.ch/ProductDetail/710-150040VS73220)
- [Würth 150040YS73220 1mm x 0.5mm yellow](https://www.mouser.ch/ProductDetail/Wurth-Elektronik/150040YS73220)
- [Würth 150040YS73240 1mm x 0.5mm yellow](https://www.mouser.ch/ProductDetail/Wurth-Elektronik/150040YS73240)
- [Kingbright APHHS1005SYCK 1mm x 0.5mm yellow](https://www.mouser.ch/ProductDetail/Kingbright/APHHS1005SYCK)
- [Bivar SM0402YC 1mm x 0.5mm yellow](https://www.mouser.ch/ProductDetail/Bivar/SM0402YC)
- [Lumex SML-LX0402SYC-TR 1mm x 0.5m yellow](https://www.mouser.ch/ProductDetail/Lumex/SML-LX0402SYC-TR)
- [ROHM SML-P12YTT86R 1mm x 0.6nn yellow](https://www.mouser.ch/ProductDetail/ROHM-Semiconductor/SML-P12YTT86R)

Alt Components

- [IS31FL3730 8x8 matrix output](https://www.mouser.ch/ProductDetail/Lumissil/IS31FL3730-QFLS2-TR)
- Optional [BMM150 Magnotometer](https://www.bosch-sensortec.com/products/motion-sensors/magnetometers-bmm150/)
- [Bosch Sensortech BHI160B]() - [Mouser](https://www.mouser.ch/ProductDetail/Bosch-Sensortec/BHI160B?qs=qSfuJ%252Bfl%2Fd4gguUCihLWmA%3D%3D)

Connectors placed on the board are,

- 2 * [Molex 22PIN 0.5mm pitch 54548-2271](https://www.molex.com/molex/products/part-detail/ffc_fpc_connectors/0545482271)
- 2 * [Hirose DF40C-34DS-0.4V](https://www.hirose.com/en/product/p/CL0684-4023-0-51) ([Mouser](https://www.mouser.ch/ProductDetail/Hirose-Connector/DF40C-34DS-04V51?qs=vcbW%252B4%252BSTIpg26DsEbj1iQ%3D%3D))
- 1 * [TE Connectivity 45PIN 0.3MM 571-4-2328724-5 FPC 3-2328724-5](https://www.te.com/usa-en/product-4-2328724-5.html) $0.41

 
Articles

- [Led PCB Circuit Board](https://www.raypcb.com/led-pcb-board/)
- [Uncovering PCB Embedded Components](https://resources.pcb.cadence.com/blog/2022-uncovering-pcb-embedded-components)
- [Practical steps for creating embedded components with side-emitting LEDs](https://resources.altium.com/p/practical-steps-for-creating-embedded-components-with-side-emitting-leds)
- [Efficient LED Blinking for Embedded Systems](https://www.electronicsforu.com/electronics-projects/efficient-led-blinking-for-embedded-systems)
- [Embedding of Passive Components into Flex PCB](https://www.pcbway.com/blog/PCB_Basic_Information/Embedding_of_Passive_Components_into_Flex_PCB.html)
- [LED module design considerations for an aluminium board](https://electronics.stackexchange.com/questions/153513/led-module-design-considerations-for-an-aluminium-board)
- [Led Bar array with stm32f103 microcontroller](https://www.engineersgarage.com/led-bar-with-stm32-microcontroller/)
- [APA102 2020 RGB LED source](http://addressable-led.com/Products/APA102-2020-LED.html)
- [Novel control strategy for synchronous PWM on a matrix converter](https://www.researchgate.net/publication/224077571_Novel_control_strategy_for_synchronous_PWM_on_a_matrix_converter)
- [Adafruit 16x9 Charlieplexed PWM LED Matrix Driver - IS31FL3731](https://www.adafruit.com/product/2946)


## Camera connectors

Two sets of camera connectors are on the board for left and right sides respectively.
The 22 pin connector allows a Development board to be connected with a Raspberry Pi Zero compatible flex cable.
The 34 pin connector allows attachment of a 201 Camera Module made for it.
Signals will be transferred directly between the two connectors using voltage shifters

## Power

Self powered
Always on
Power module connected


## LED layout

LEDs are laid out as eyebrows and a mouth. They are connected to the multiplexer as 7 sets of 9 LEDs (7x9 mode).
1) Brow x 2
1) Eye sides x 2 (reverse of brow signal)
3) Smile x 2
5) Sad x 2 (reverse of smile signal)
7) Cheeks, split 4 left 4 right.

Numbering of individual LEDs are from top-left to right.
The eyebrow sets are doubled up with the eye side using reverse polarity. The eye sides get signals from VIAs close to the eye hole.

The smile if formed by a left side and a right. LED numbering starts in the middle.
A sad smile uses the same multiplexer banks but with reverse polarity.

LEDs are marked with identifiers on the connector side, but not on the front side.



Vias around nose and hair

I2C3 breakout
Power breakout

Connecting LP5036 on I2C3

I2C3 on sound connector?


### LED mounting

Most LEDs are mounted by embedding them into the board. The PCB being 1mm thick a recess is made to fit the LED of 0.4mm. In the center a 0.4mm hole is drilled to let through light.


## MotionEngine I2C Sensor

The BOSCH sensor includes an embedded processor communicating via I2C. It boots from a 1MB flash chip. It runs and communicates on is 1.8V.

https://www.mouser.ch/ProductDetail/Bosch-Sensortec/BHI260AP?qs=T94vaHKWudTEPTnGI%252BTy9w%3D%3D

BHI260AB I2C modes support 3.4 Mbit/s. Put on SYS or 3 ? HSCX + HSDX. i.MX 8 can only do 400KHz.

Power comes from any of the SOM lines via the two 50 pins connectors. Isolate them and down regulate to 3.3V.

Host I2C is I2C3 on the CPU side.
Master I2C 2 is I2C6 on the CPU side, Right CAM CSI2 SCCB & Ambient Light.
Master I2C 3 is I2C5 on the CPU side, Left CAM CSI1 SCCB & Laser Scan.
Master is is free for SPI communication.

Sensor linux driver source - https://github.com/BoschSensortec/BHY2-Sensor-API

? Event interrupts vs GPIO
? Timers
? Aux IMU I2C

| Pin | Pad      |                    | to        |  
|-----|----------|--------------------|-----------|
| 1   | M3SDA    | Left CSI1 I2C SDA  | SOM I2C5  |
| 2   | M3SCL    | Left CSI1 I2C SCL  | SOM I2C5  |
| 3   | HOSTBOOT | System Control     | EX0          |
| 4   | QSPI_D0  | Flash              | Flash chip          |
| 5   | QSPI_CLK | Flash              | Flash chip |
| 6   | VREG     | Supply             |           |
| 7   | VDDIO    | Supply             |           |
| 8   | QSPI_D3  | Flash              | Flash chip |
| 9   | RESETN   | System Control     | EX0.       |
| 10  | HIRQ     | Host I2C IRQ       | SOM I2C3 / EX0  |
| 11  | HSDX     | Host I2C SDA       | SOM I2C3  |
| 12  | VDDIO    | Supply             |           |
| 13  | M2SCX    | Right CSI2 I2C SCL | SOM I2C6  |
| 14  | QSPI_CSN | Flash              | Flash chip |
| 15  | QSPI_D1  | Flash              | Flash chip |
| 16  | MCSB3    | GPIO / Chip Select 3 | Breakout |
| 17  | GND      | Supply             |        |
| 18  | MCSB2    | GPIO / Chip Select 2 | Breakout |
| 19  | MCSB4    | GPIO / Chip Select 4 | Breakout |
| 20  | QSPI_D2  | Flash              | Flash chip |
| 21  | OCSB     | IMU Auxiliary      | BMM150     |
| 22  | ASCX     | IMU Auxiliary      | BMM150     |
| 23  | JTAG_CLK | Debug               | Breakout  |
| 24  | JTAG_DIO | Debug               | Breakout  |
| 29  | M1SCX    | Master 1 I2C SCL  | Breakout |
| 30  | ASDX     | IMU Auxiliary      | BMM150     |
| 33  | HSCX     | Host I2C SCL       | SOM I2C3  |
| 37  | M2SDI    | GPIO               | M2SDI |
| 38  | MCSB1    | GPIO / Chip Select 1 | Breakout |
| 39  | ASCX     | IMU Auxiliary      | BMM150     |
| 43  | M1SDI    | GPIO SPI Master 1  | Breakout |
| 44  | M1SDX    | Master 1 I2C SDA   | Breakout |






Address

HSDO is LSB selecting 0x28 or 0x29



Need to add CM36686 proximity and ambient light sensor?

http://www.capellamicro.com.tw/EN/product_c.php?id=85&mode=16&search=

https://www.kynix.com/Detail/104230/CM36686M3OE.html


https://community.bosch-sensortec.com/t5/MEMS-sensors-forum/BNO055-vs-BHI260AB-fusion-accuracy/td-p/24263


### QSPI Flash
CLK
CSN
D0..D3

Quad SPI / QPI modes
0.5 - 8 MBytes supported

Voltage? Winbond?


## Other sensors

Accelerator / Gyro
FXAS21002


Ambient light

Down regulator 4V / V_SOM -> 3.3V



## 3D Model libraries

https://kicad.github.io/packages3d/


