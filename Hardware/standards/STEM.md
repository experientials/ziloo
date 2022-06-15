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

:[Stem I2C addresses](../pinouts/STEM_I2C_ADDRESSES.md)

:[SYS I2C addresses](../pinouts/SYS_I2C_ADDRESSES.md)

