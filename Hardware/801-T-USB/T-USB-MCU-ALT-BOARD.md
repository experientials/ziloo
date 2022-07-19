# T-USB MCU Alt. Board

The T-USB board has two 45 pin Alt. Connectors that provide the ability to hook in to the core of the board.
The MCU will be integrated in the production version of the T-USB board, but for development and testing it
will remain separate. 



## T-USB OTG alt mode connector

The MCU connects primarily through the OTG Alt mode connector pins 19 to 45.
These connectors(only on the development model) enables experimentation with alternate modes and directional pins.

:[45 pins T-USB OTG alt mode connector](../pinouts/T-USB_OTG_ALT_CONNECTOR.md)

The RP2040 is powered by 3V3(1, 4, 7) and GND(16, 30, 33) from the connector.


## Firmware

The firmware on the RP must select a number of known devices primarily via the I2C bus.

### Ziloo Autonomous App

The App is a Git Repo codebase as a Zephyr Workspace App with

- Custom Board Definitions
- Explicit port definitions for all the relevant pins
- Device drivers for common sensors
- Integration of MicroPython allowing scripts to be run


### Activity Device (/dev/activity)

:[Activity Device](../refs/ACTIVITY_DEVICE.md)


### Broadcom APDS-9960 Proximity Light and Gesture Sensor

On Night I2C on address 0x39.

Testing:
- https://upy-apds9960.readthedocs.io/en/latest/


### PCA9555 I/O Expander

On Stem I2C on address 0x23

Refs
- https://github.com/dfletcher/avr-pca9555
- [Sample Board with a PCA9555 MEC15xxEVB ASSY6853](https://docs.zephyrproject.org/latest/boards/arm/mec15xxevb_assy6853/doc/index.html)


### IS31FL3730 8x8 LED matrix

On Stem I2C

https://github.com/PastravMD/microdot-phat-driver

- [Adafruit breakout board](https://www.adafruit.com/product/2946)
- 

### TPS65988 PD Controller

On Stem I2C


### BQ24250RGER battery charger

On Stem I2C


### Virtual OTG USB Comm ports 

- UART1 .. UART4 as individual devices available on the USB 2.0


### VM3011 Multi-mode microphone

- Connected via PDM pins
- Interrupts on sound

[Create a USB Microphone with the Raspberry Pi Pico](https://www.hackster.io/sandeep-mistry/create-a-usb-microphone-with-the-raspberry-pi-pico-cc9bd5)


### MC6470 Motion Sensor

On Stem I2C on address 0x4C


### DVP parallel camera interfacing over SPI or SCCB imaging

https://www.arducam.com/raspberry-pi-pico-tensorflow-lite-micro-person-detection-arducam/

https://maker.pro/arduino/tutorial/how-to-interface-the-ov7670-camera-module-with-arduino


### TinyML

- Zephyr
- CircuitPython


## Stem I2C addresses

:[Stem I2C addresses](../pinouts/STEM_I2C_ADDRESSES.md)


## Pico / RP2040 pin mapping

:[RP2040 pin mapping](../pinouts/RP2040_PIN_MAPPING.md)


## Additional pins

A header needs to break out pins for connection to Host Alt Connector or others.
The header also needs to break out the OTG Alt. Mode lanes and Extra pair.

| 31  | SWD CLK RP       |          |                                      |         |
| 32  | SWD DAT RP       |          |                                      |         

