The Ziloo Stem is implemented by the central RP2040, a dual core Cortex M0+ that controls the running state and power of many parts of the system.

The Stem I2C is used to get input from sensors, which is used to determine the waking state.

The Nighttime I2C is used to get ambient light sensor input and to provide a command point for SoM when awake.

The Stem could work without sharing I2Cs by using the CAN bus.



System I2C

Enables/disables features of the different circuits.


Stem I2C

Controls power, sensors and LEDs that are fully autonomous.
RP2040 is master.
Sensors are placed on the faceboard.
EX3 is on the T-USB board.

Pins: STEM_SCL, STEM_SDA, STEM_INT


Nightime I2C

Sensors used to determine that Ziloo needs to wake up.

Pins: CSI2_SCL, CSI2_SDA, CSI2_INT


## Nighttime camera (IR)

The nighttime camera sits in the right side and uses a lens without a filter(or one that lets through IR).
The sensor is oriented in landscape orientation to capture the widest FoV horizontally. The lens will capture 120°.
The sensor is connected to CSI2.
The SBBC is I2C6


## Human sensor

Dedicated lines


## VM3011 wake on sound

Three lines for PDM. CLK, DATA, IRQ

https://www.hackster.io/sandeep-mistry/create-a-usb-microphone-with-the-raspberry-pi-pico-cc9bd5

VM3011 is a high performance, low noise digital MEMS microphone.


## I2C adressing


Stem I2C addresses

| Address    | Chipset  | Description                             |
|————————-———|-——————-——|———————--------------------------------——|
| 0x7E 0x7F  | TPS65988 |  PD Controller Port 2                   |
| 0x23       | PCA9555  | 16 bit expander EX3/T-USB daughterboard |
| 0x24       | PCA9555  | 16 bit expander EX4/faceboard           |
| 0x28       | BHI260AP | Motion Engine (alternate config)        |
| 0x40/0xC0 or 0x44| IS31FL3730 | LED controller                  |      
| 0x4C       | MC6470   | 9-Axis Sensor                           |
| 0x54..0x57 | EEPROM   | Faceboard EEPROM          |
| 0x60       | VM3011   | mic           |
| 0x6A       | BQ24250  | LiPO Battery Charger      |
| 0x98 0x99  | MC6470   | 9-Axis Sensor


SYS I2C addresses

| Address    | Chipset  | Description               |
|————|-———|—————————|
| 0x20       | PCA9555  | 16 bit expander EX0       |
| 0x21       | PCA9555  | 16 bit expander EX1/USB1  |
| 0x22       | PCA9555  | 16 bit expander EX2/USB2  |
| 0x68       | PI6CG18200 | PCIe clock generator |
| 0x70 0x71  | TPS65988 |  RESERVED for PD Controller Port 1 / SYS |
| 0xD2/D3    | RTC      | AM1805 real time clock (RTC) |



       |