# Testing Hardware

Ziloo and Talki can be tested and controlled by inserting a **Testing Shim PCB** between the main board and the T-USB daughterboard. This allows control of
the 2 * 50 pin connectors. The Testing ship enables attaching a Raspberry Pi 4 or Raspberry Pi Pico with OpenOCD/Picoprobe firmware.

- The Stem MCU UART0 console output can be accessed via the Probe USB connector.
- The Stem MCU SWD debug connection
- The Probe UART0 and SWD connections are left unconnected
- The Probe and RPi4 can directly access sensors on Night and Stem I2C
- The Probe and RPi4 can simulate SoM use of SYS I2C
- RPi4 can access SoM UART1/3
- The Probe makes SoM UART2/4 available over USB
- The Probe and RPi4 can test SDIO access to m.2 WiFi module and SD Card reader




### Uploading firmware to Picoprobe



### Uploading firmware to Stem MCU



### Connecting Stem MCU


### Raspberry Pi Pico 2 x 20 pins sockets


### Raspberry Pi 40 pin GPIO connector

JTAG for the SoM is mapped to SPI pins. Hopefully it can allow for high speed transfer. 
TDI goes from controller to tested device, sounds like MOSI.
TDO goes from last testing device to to the controller, sounds like MISO.
BCM2711 Alt modes maps to SPI1/SPI6.


### Additional Headers



- [Pico buck converter Richtek RT6150](https://www.richtek.com/Products/Switching%20Regulators/Buck-Boost%20Converter/RT6150ART6150B?sc_lang=en&specid=RT6150A/RT6150B)
- 