## Dual camera module

The bridge board connects two camera modules that can be run in sync. The modules are largely identical, but do differ.
To support stereo vision as an option the two cameras use the same type of lens in order to capture two images with
the same physical translations.
The plan is to use a fixed lens. Testing so far has not shown auto-focus to be needed.

I assume that all 4 sensors will be on the same SCCB/I2S bus with unique addresses.


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

For debugging a separate appendage should be added following the RPi 15 pin 1mm FFC connector.


## Components

* 2 * OV2732 or similar
* APDS-9960 sensor above IR camera
* VL53L1 sensor above RGB camera
* 2 * [CMM-4030D-261-I2S-TR microphone](https://www.cuidevices.com/product/audio/microphones/mems-microphones/cmm-4030d-261-i2s-tr) 


### SCCB / I2C addresses

- Left Image Sensor
- Right Image Sensor
- APDS-9960
- VL53L1

Omnivision SCCB ID select
0: 0x20 - RGB daytime
1: 0x6C - IR nighttime

Since the image sensors are oriented on the FFC board they can be hardcoded to their ID


## Synchronised Dual Image Sensors Diagram (Job)

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



## Hirose DF40 single eye connector 34/40 pins

- DF40C-34DS-0.4V(51) Receptacle
- DF40C-34DP-0.4V(51) Plug

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

## Connector pinouts 45 pins connector (alternate connector idea)

Connected sensors are

* RGB camera sensor OV2732 with filter
* IR camera sensor OV2732 without filter
* VL530X ToF sensor
* APDS-9960 Proximity/Ambient Light sensor

I2C-bus Fast Mode Compatible Interface 400kHz 1.8V signal

Board-to-Wire FPC 45 pin connector 0.3mm pitch

TODO I2C register switching mems microphones on/off
TODO I2C switch cameras on/off

MIPI 2 lanes interface like https://wiki.somlabs.com/index.php/SL-MIPI-CSI-OV5640_Datasheet_and_Pinout

* [TE 45 pins Wire-to-Board FPC 0.3 4-2328724-5](https://www.te.com/usa-en/product-4-2328724-5.html) [Mouser](https://eu.mouser.com/ProductDetail/TE-Connectivity/4-2328724-5?qs=w%2Fv1CP2dgqow3y3efq3sig%3D%3D) $0.41



Pin Pin Name            Default function                                IO Power domain   Pad type IO pull
1 AVDD_2V8                2.8V OUTPUT, Max 500mA            IR_AVDD 2.8V
2 VCC3V3_SYS            3.3V OUTPUT, Max 500mA              RGB_AVDD        3.3V
3 GND                    GND                                Power ground
4 VL53L1 INT             Interrupt VL53L1, Active L         Interrupts        1.8V?
5 APDS-9960 INT          Interrupt APDS-9960, Active L      Interrupts        1.8V?
6 I2C1_SCL                I2C1_SCL(pullup resistor 2.2K)    IR+RGB            1.8V         UP
7 I2C1_SDA                I2C1_SDA(pullup resistor 2.2K)    IR+RGB             1.8V         UP
8 GND                    GND                                Power ground
9 MIPI_CSI_CLK0            MIPI_CSI_CLK0 OUTPUT (Strobe?)   For IR Camera        1.8V DOWN
10 GND                    GND                                Power ground
11 MIPI_CSI_RX0_CLKP        MIPI_CSI_RX0_CLK+                For IR Camera     1.8V
12 MIPI_CSI_RX0_CLKN        MIPI_CSI_RX0_CLK-                For IR Camera      1.8V
13 GND                    GND                                Power ground
14 MIPI_CSI_RX0_D0P        MIPI_CSI_RX0_D0+                  For IR Camera        1.8V
15 MIPI_CSI_RX0_D0N        MIPI_CSI_RX0_D0-                  For IR Camera         1.8V
16 GND                    GND                                Power ground
17 MIPI_CSI_RX0_D1P        MIPI_CSI_RX0_D1+                  For IR Camera            1.8V
18 MIPI_CSI_RX0_D1N        MIPI_CSI_RX0_D1-                  For IR Camera            1.8V
19 GND                    GND                                Power ground

20 BCLK / SCK            Bit clock line                     Microphone I2S        1.8V
21 WS / LRCLK            Word clock line                    Microphone I2S        1.8V
22 SDATA1                Input data 1                       Microphone I2S        1.8V
23 SDATA2                Input data 2 (NC)                  Microphone I2S        1.8V
24 PWM 1                 NC                                 Motor
25 PWM 2                 NC                                 Motor
26 reserved
27 EXPANDER RESET          Reset I/O Expander, Active L     Module Reset  (DOWN/UP ?)

28 GND                    GND                                Power ground
29 DVDD_1V2                1.2V OUT ,MAX 300mA                For OV2718/32/40 Camera            1.2V
30 VCC_1V8                1.8V OUT ,MAX 200mA                IR+RGB                    3.3V
31 GND                    GND                                Power ground
32 MIPI_CSI_CLK1            MIPI_CSI_CLK1 Output            For RGB Camera            1.8V        DOWN
33 GND                    GND                                Power ground
34 MIPI_CSI_RX1_CLKP        MIPI_CSI_RX1_CLK+                For RGB Camera            1.8V
35 MIPI_CSI_RX1_CLKN        MIPI_CSI_RX1_CLK-                For RGB Camera            1.8V
36 GND                    GND                                Power ground
37 MIPI_CSI_RX1_D0P        MIPI_CSI_RX1_D0+                  For RGB Camera            1.8V
38 MIPI_CSI_RX1_D0N        MIPI_CSI_RX1_D0-                  For RGB Camera            1.8V
39 GND                    GND                                Power ground
40 MIPI_CSI_RX1_D1P        MIPI_CSI_RX1_D1+                  For RGB Camera            1.8V
41 MIPI_CSI_RX1_D1N        MIPI_CSI_RX1_D1-                  For RGB Camera            1.8V
42 GND                    GND                                Power ground
43 MIPI_CSI_RX1_D2P        MIPI_CSI_RX1_D2P                  For RGB Camera            1.8V
44 MIPI_CSI_RX1_D2N        MIPI_CSI_RX1_D2N                  For RGB Camera            1.8V
45 GND                     GND                                POWER GROUND


## XSHUT I2C Address

Due to the number of sensors we consider an I/O expander. The power overhead must be considered.

* [XRA1201/1201P 16-BIT I2C/SMBUS GPIO EXPANDER](https://eu.mouser.com/ProductDetail/MaxLinear/XRA1201IL24TR-F?qs=06nTM9U4TTbOGDwXPyhb6A%3D%3D)$1.4
* [Texas TCA6408AQPWRQ1](https://eu.mouser.com/ProductDetail/Texas-Instruments/TCA6408AQPWRQ1?qs=dn2ehRJXTX%252BDd5mX8WZrSw%3D%3D) $1.5


Features

* RGB camera XSHUTDOWN
* RGB camera XSHUTDOWN2
* RGB camera PWRDN
* IR camera XSHUTDOWN
* IR camera XSHUTDOWN2
* IR camera PWRDN
* Enable camera sync
* VL53L1 XSHUTDOWN

Note: Reset/XShutdown is inverted. False = High, True = Low

TODO check that voltage level 1.8V is supported for the chosen chip
TODO Check interrupt signal voltages of sensors
TODO List of I2C adresses


* [Samsung Camera Module Guide](https://www.samsungsem.com/global/product/module/camera-module.do)
* [Tele Camera Module - Vertical 13MP]()
* [M8 Stereo 3D OV4689 USB](http://www.camera-module.com/product/duallenscameramodule/smallest-dual-lens-stereo-3d-camera-module-ov4689.html)
* [Lumia 925 Lens Assembly](http://mynokiablog.com/2013/07/04/pics-detailed-lumia-925-lens-assembly-high-resolution-images/)


