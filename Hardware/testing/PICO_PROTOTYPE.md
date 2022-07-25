# Raspberry Pi Pico prototype

The aim is to develop a well working prototype based on Raspberry Pi Pico (* 2).
It should not fall apart when used, so wires must have robust connections.
It would be built on universal PCB soldered or wire-wrapped.
It should use connectors to all reconnecting and expanding with additional boards.

It must wire up,

- RCWL-0517 radar body sensor (https://dronebotworkshop.com/rcwl-0516-experiments/)
- [VM3011 MEMS microphone](https://www.digikey.ch/en/products/detail/vesper-technologies-inc/VM3011-U1/13165343) ([Dev board S-VM3000-C](https://www.mouser.ch/ProductDetail/Vesper/S-VM3000-C?qs=uwxL4vQweFOlo6Cyc08Elw%3D%3D))
- [MC6470 motion sensor](https://mcubemems.com/product/mc6470-6-axis-ecompass/) ([Breakout board 6DOF IMU 9 CLICK](https://www.mikroe.com/6dof-imu-9-click))
- [APDS-9960 Ambient light sensor](https://www.mouser.ch/ProductDetail/Broadcom-Avago/APDS-9960?qs=9j6qqDjiC68hPiaH59tKpQ%3D%3D) ([Breakout board](https://learn.adafruit.com/adafruit-apds9960-breakout))
- NFC antenna via I2C
- Battery voltage measuring of external battery
- Headers for measuring power consumption


Parts of the prototype

- Pico sensing with RCWL-0517, VM3011, MC6470, APDS-9960 and NFC antenna. (as available)
- Pico programmer based on [Picoprobe](https://github.com/raspberrypi/picoprobe), [How-to](https://www.digikey.ch/en/maker/projects/raspberry-pi-pico-and-rp2040-cc-part-2-debugging-with-vs-code/470abc7efb07432b82c95f6f67f184c0).
- Software source code as Git repository
- A physical setup with two Picos on separate boards
- Instructions/Notes on how to run it in the Git repository


## I will supply you with

- Ten universal PCBs 50x70 mm 18x24
- 5 * PCA9555 breakout boards
- 5 * VM3011 S-VM3000-C
- 3 * MC6470 (6DOF IMU 9)
- 5 * apds9960-breakout
- 2 * NFC antennas
- LiPo Battery to test
- Cables / connectors
- Micro SD card

You must already have a raspberry pi to test with and purchase 10 Raspberry Pi Picos along with any additional supplies.


## Milestones $310 + 150

1. Receive the components $10
2. Create a working prototype $100
3. Verify that components are reachable using CircuitPython or Rust $100
4. Create 4 more prototypes $100
5. Send everything to me (5 sets of prototypes) $150 to cover shipping and Pico purchase

I need a report on the findings including

- Sample source code
- Explicitly how to in connecting to sensors and reading data
- Enumeration of available sensors


## I/O Expander

The T-USB Pico connects to a PCA9555 I/O Expander that captures sensor interrupt signals(RIGHT_ATT_INT, IMU_INTM, IMU_IRQ,VM3011 DOUT). The expander is connected to Stem I2C and triggers the Stem INT pin.

:[Expander](../pinouts/I2C_EXPANDER_4.md)


## Connecting Sensors

Sensors are either connected directly(VM3011, RCWL-0517) or via Stem I2C.

:[I2C Addresses](../pinouts/STEM_I2C_ADDRESSES.md)


![Universal PCB](../refs/universal-PCB.jpg)


## Connecting multiple MCUs

The boards are connected using a 2x20 pin header.

TODO drawing of multiple boards connected


## Firmware

Implement test firmware with Rust or CircuitPython

The software should idle with low power when nothing happens and wake up to
respond to sensor input. The implementation should create an event object on IRQ
and pass on to a configurable handler chain.




## Probe part

The probe part runs on a dedicated Pico board.
Use an Univeral PCB with connectors for stability and connectors that allow attaching different boards.

Connectors
- 10 pin header SWDCLK, SWDIO, UART2, UART4, Probe UART, GND (to two connectors)
- Inter MCU bus header

## Connect Camera

Connect to an image sensor using the least amount of pins in addition to SCCB(I2C) interface.
The purpose is to be able to capture low resolutions still images for simple motion detection using

See PDF


### DVP parallel camera interfacing over SPI or SCCB imaging

[Raspberry Pi Pico Wiring Camera](https://learn.adafruit.com/capturing-camera-images-with-circuitpython/raspberry-pi-pico-wiring)

https://www.arducam.com/raspberry-pi-pico-tensorflow-lite-micro-person-detection-arducam/

https://maker.pro/arduino/tutorial/how-to-interface-the-ov7670-camera-module-with-arduino

https://www.tinyml.org/event/summit-2021/

https://www.tinyml.org/event/summit-2022/

https://www.arducam.com/product/arducam-pico4ml-tinyml-dev-kit-rp2040-board-w-qvga-camera-lcd-screen-onboard-audio-b0330/



## Pico Pin allocation

:[Pin allocations](../pinouts/RP2040_PIN_MAPPING.md)


## Communicating between two RP2040s

Two Picos should be wired up with common pins to test SPI/I2C/CAN/QSPI/SDIO data exchange.

SDIO GPIO header pins 13, 15, 16, 18, 22, 37 (suggested)
SDIO UCM i.MX8 pins P2 92, 94, 96, 97, 98, 99, 100

To interface with SoM should multiple pins be connected (SPI + SDIO). I.E. P2.89 to P2.97 ?

Twisted MOSI - MISO


- [Protocol Info](https://fmuser.org/news/IPTV-encoder/Introduction-to-SPI-I2C-UART-I2S-GPIO-SDIO-CAN/)
- [Raspberry Pi SDIO connections](https://pinout.xyz/pinout/sdio)
- [SPI Accessing the SD Card](https://luckyresistor.me/cat-protector/software/sdcard-2/)
- [Secure Digital (SD) pinouts](https://pinoutguide.com/Memory/sdcard_pinout.shtml)
- [Raspberry Pi 4 GPIO functions](https://elinux.org/RPi_BCM2711_GPIOs)
- 


Lines on the zimbus,

- SDIO CD / SPI CS (only on SD card)
- SDIO CMD / SPI MOSI (.13 SPI1 TX) - verfy? 
- SDIO CLK / SPI CLK (.12 SPI1 SCK)
- SDIO DATA0 / SPI MISO (.30 SPI1 RX) - verify?
- SDIO DATA1 (.16 SPI0 RX)
- SDIO DATA2 (.17 SPI1 TX)
- SDIO DATA3 (.24 SPI0 SCK)
- STEM INT (.4)
- STEM SCL (.19)
- STEM SDA (.18)
- NIGHT INT (.5)
- NIGHT SCL (.21)
- NIGHT SDA (.20)
- SYS SCL (.7)
- SYS SDA (.6)

SD Card must ignore other pins if Card Select(CS) isn't enabled.
All MCUs must monitor the Card Select(CS) to see if other MCU is running SDIO mode.

- One MCU locks bus in SDIO and becomes master
- 

### MCU cluster

(?) Structure of SoM with multiple low power MCUs around


### SYS I2C bus

The SYS bus is normally managed by the i.MX SoM, so the RPs will normally do nothing with it.
However they have pins allocated to allow taking over

### Stem I2C bus

The Stem I2C is used to identify connected boards and coordinate the bus setup.
Each board will have an EEPROM with unique keys or emulate one with the MCU. 
Each one with a different address.
MCUs on Stem I2C must act as slaves in the address range 0x70 - 0x7f (or 10 bit space?)

To make changes an MCU must write to all other MCUs in the range the address of the
MCU taking charge. When done it must write 0 to the same MCUs.
When booting an MCU must listen for activity on the data pin for 3 sec before trying to
take charge. MCU in charge must use the bus at least once every 2.5 sec.
Should there be a time limit to being in charge?

The Stem I2C is accessable on the SoM as I2C3.

An MCU can take charge of,

- SDIO access to SD Card / MMC
- Night I2C
- Monitoring Sensors on the Stem I2C

Chip enable via I/O Expander


### NFC Testing

[NFC Antenna Design Made Easy](https://www.nxp.com/company/blog/nfc-antenna-design-made-easy:BL-NFC-ANTENNA-DESIGN-MADE-EASY)

[NFC Antenna Design Hub](https://www.nxp.com/products/rfid-nfc/nfc-hf/nfc-readers/nfc-antenna-design-hub:NFC-ANTENNA-DESIGN-TOOL)


### Setup with Raspberry Pi 400 / 4



### MCU I2C slaves on the Stem

Information readable

- Time since startup (16 bit)
- Which address is master (16 bit)
- Product Key


Test SDIO against

- SD Card slot
- MMC
- BT/WiFi modules
- [WiFi 5 m.2 Key B](https://www.sparklan.com/product/wnfq-262acnibt-qca6174a-b-key-industrial-module-sparklan/)
- [WiFi 6 m.2 Key E](https://www.sparklan.com/product/wnfb-266axibt-broadcom-wifi6-industrial-sdio-m-2-module/)

I/O Extender Stem

SPI/SDIO slaves

- SD Card reader
- SPI Display
- m.2 WiFi module



- SCCB parallel camera such as OV2710


- Camera Pico that connects to Image sensors
