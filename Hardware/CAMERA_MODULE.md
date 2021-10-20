# Dual camera module

The bridge board connects two camera modules that can be run in sync. The modules are largely identical, but do differ.
To support stereo vision as an option the two cameras use the same type of lens in order to capture two images with
the same physical translations.
The plan is to use a fixed lens. Testing so far has not shown auto-focus to be needed.

I assume that all 4 sensors will be on the same SCCB/I2S bus with unique addresses.

### Open points / tasks

- Plan the wiring diagram for dual camera setup with relevant sensors for reference
- Review the connector pins
- Do full diagram of Sensor module with ToF/Ambient sensors and microphone
- List of possible places to produce small batches (10 - 100)
- Should lens be attached to module by producer, or easy to do ourselves?
- FFC Board design
- Testing/QA with/without bridge board


### Synchronised Dual Image Sensors Diagram (Job)

You should have experience with image sensors and have access to full datasheets from the manufacturers.
I am currently looking at OV2732/35, but am open to other suggestions.

The aim of this job is to produce,

- a diagram with two image sensors
- suggestion for sensors with 1080p low light video capture capability
- reasoning for sensor choices
- datasheets for the proposed sensors
- details on which pins to expose to the receiving/controlling MCU
- details on clocks to connect

The diagram must connect the two sensors to capture video in sync.
The two sensors can be different as one is focused on daytime and the other on nighttime.

![Camera Module connected](./camera-module-connected.png)


## Daytime camera (RGB)

The daytime camera sits at the left side and uses a lens with a filter(only letting through visible light).
The sensor is oriented in portrait orientiation to capture people and activity looking down or up at the device.
The lens will capture 120°.
The sensor is connected to CSI1.

On the outside edge(left) of the lens a Time-of-Flight(VL53L1) sensor is attached to scan and capture the depth straight ahead.

The module also contains a MEMS microphone.


## Nighttime camera (IR)

The nighttime camera sits in the right side and uses a lens without a filter(or one that lets through IR).
The sensor is oriented in landscape orientation to capture the widest FoV horizontally. The lens will capture 120°.
The sensor is connected to CSI2.

On the outside edge(right) of the lens an Ambient light(APDS-9960) sensor is attached to sens general level and color of light.

The module also contains a MEMS microphone.


## Modes

The cameras will typically be used one at a time. By default the daytime camera is used, and in low light the nighttime camera.
It must be possible to switch both cameras on and capture in sync(FSIN).
It must be possible to switch off both cameras to save power while still using the Ambient light sensor via I2S.


## Image qualities

The device captures images and low speed video to be consumed by machines. This means that while the captures must be sharp, the color
must not be true. Not for human estethics, but rather for machine interpretation.

Since the images must be processed on device with many algorithms the resolution will never be high. A maximum of 1080p seems to be a good tradeoff.


## Connectors

The module is connected to the bridge board using a Hirose DF40 single eye connector 34/40 pins.

For debugging a separate appendage should be added following the RPi 15 pin 1mm FFC connector, which can be scissored off.


## Components

* OV2732 or similar
* APDS-9960 sensor above IR camera
* VL53L1 sensor above RGB camera
* [CMM-4030D-261-I2S-TR microphone](https://www.cuidevices.com/product/audio/microphones/mems-microphones/cmm-4030d-261-i2s-tr) 
* DF40C-34DP-0.4V(51) Plug (fits into DF40C-34DS-0.4V(51) Receptacle)



### SCCB / I2C addresses

- Left Image Sensor
- Right Image Sensor
- APDS-9960
- VL53L1

Omnivision SCCB ID select
0: 0x20 - RGB daytime
1: 0x6C - IR nighttime

Since the image sensors are oriented on the FFC board they can be hardcoded to their ID


## Hirose DF40 single eye connector 34/40 pins

1  AF_VDD     Power    Autofocus             3.3V ?
3  AVDD_2V8   Power    Analog 2.8V OUTPUT, Max 500mA
5  AVDD_2V8   Power    Analog 2.8V OUTPUT, Max 500mA
7  DOVDD      Power    Power for I/O circuit, Max 300mA        1.8V
9  EXTCLK      Input   External Clock Input
11 DVDD_1V2   Power    1.2V  ,MAX 300mA                   For OV2718/32/40 Camera            1.2V
13 VCC_1V8    Power    1.8V ,MAX 200mA                                       1.8V
15 XSHUTDOWN  Input    Camera Reset, Active Low   
17 PWRDN      Input    Camera Power Down
19 CAM_SID    Input    Sensor slave address selection input   (tentative)
21 I2C_SCL    I/O      I2C1_SCL(pullup resistor 2.2K)                    1.8V         UP
23 I2C_SDA    I/O      I2C1_SDA(pullup resistor 2.2K)                    1.8V         UP
25 CAM_FSIN   I/IO     Frame sync input
27 Reserved
29 ATT_INT    Output   Interrupt Attached Sensor, Active L    Interrupts        1.8V?
31 ATT_XSHUT  Input    Attached Sensor XSHUTDOWN                                    1.8V
33 Reserved

35 Reserved                                                               GND
37 Reserved
39 Reserved

2  Reserved (NC)         PWM Motor control
4  BCLK / SCK            Bit clock line                     Microphone I2S        1.8V
6  WS / LRCLK            Word clock line                    Microphone I2S        1.8V
8  SDATA1                Input data 1                       Microphone I2S        1.8V
10 SDATA2                Input data 2 (NC)                  Microphone I2S        1.8V
12 -                                                                      GND
14 MIPI_CSI_RX_CLKP      MIPI_CSI_RX_CLK+                For Camera     1.8V
16 MIPI_CSI_RX_CLKN      MIPI_CSI_RX_CLK-                For Camera      1.8V
18 -                                                                       GND
20 MIPI_CSI_RX0_D0P      MIPI_CSI_RX_D0+                  For Camera        1.8V
22 MIPI_CSI_RX_D0N       MIPI_CSI_RX_D0-                  For Camera         1.8V
24 -                                                                       GND
26 MIPI_CSI_RX_D1P       MIPI_CSI_RX_D1+                  For Camera            1.8V
28 MIPI_CSI_RX_D1N       MIPI_CSI_RX_D1-                  For Camera            1.8V
30 -                                                                      GND
32 MIPI_CSI_RX_D2P       MIPI_CSI_RX_D2+                  For Camera            1.8V
34 MIPI_CSI_RX_D2N       MIPI_CSI_RX_D2-                  For Camera            1.8V

36 Reserved                                                               GND
38 Reserved +
40 Reserved -


# OLD NOTES disregard ....


* [Samsung Camera Module Guide](https://www.samsungsem.com/global/product/module/camera-module.do)
* [Tele Camera Module - Vertical 13MP]()
* [M8 Stereo 3D OV4689 USB](http://www.camera-module.com/product/duallenscameramodule/smallest-dual-lens-stereo-3d-camera-module-ov4689.html)
* [Lumia 925 Lens Assembly](http://mynokiablog.com/2013/07/04/pics-detailed-lumia-925-lens-assembly-high-resolution-images/)


