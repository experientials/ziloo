# Camera Module with OV2735

We will be mounting lenses ourselves. The FFC must have holes for fitting the base and backplane

A precise drawing of the module is provided. It is essential that the module is shaped and laid out according to the drawing.
A 3D Model is also provided. This should be used for precise reference for placing the components.


## Bill of Materials

- Omnivision OV2735
- DF40C-34DP-0.4V B2B Plug (header, standard, non-shielded)
- Broadcom APDS-9960 Proximity Light and Gesture Sensors
- ToF sensor VL53L1
- CUI MEMS microphone CMM-4030D-261-I2S-TR


# Dual camera setup

The layout include two ways to mount the image sensor. Only one will be used at a time.
The current version has mounting holes for one type of M7 base.

Ideally the FFC produced should support different sizes of M7/M8 lens bases.


# ToF + Ambient sensor

The layout include two additional sensors. Only one will be used at a time

VL53L1 will be combined with image sensor oriented in portrait mode going across the FFC.
APDS-9960 will be combined with image sensor oriented in landscape mode going along the FFC.


## Diagram

Drawing & 3D Model bundled with this spec


## Layout Schematic

- All sensors are connected to either I2S or I2S bus
- Isles added to allow Mic. Select to be soldered to HIGH(1.8V) or LOW(GND)
- All connector pins(except NC / Reserved) are connected to components
- The edges around image sensors must not carry signal to allow punching extra holes for lens alignment


## Pinouts: Hirose DF40 single eye connector 34 pins


Toward thin part with microphone and other sensors

1  AF_VDD     Power    Autofocus             3.3V ?
3  AVDD_2V8   Power    Analog 2.8V OUTPUT, Max 500mA
5  AVDD_2V8   Power    Analog 2.8V OUTPUT, Max 500mA
7  DOVDD      Power    Power for I/O circuit, Max 300mA        1.8V
9  Reserved
11 DVDD_1V2   Power    1.2V  ,MAX 300mA                   For OV2718/32/40 Camera            1.2V
13 VCC_1V8    Power    1.8V ,MAX 200mA                                       1.8V
15 I2C_SCL    I/O      I2C1_SCL(pullup resistor 2.2K)                    1.8V         UP
17 I2C_SDA    I/O      I2C1_SDA(pullup resistor 2.2K)                    1.8V         UP
19 MIC SEL               Mic. Left/Right Select             Microphone I2S        1.8V
21 BCLK / SCK            Bit clock line                     Microphone I2S        1.8V
23 WS / LRCLK            Word clock line                    Microphone I2S        1.8V
25 SDATA1                Input data 1                       Microphone I2S        1.8V
27 SDATA2                Input data 2 (NC)                  Microphone I2S        1.8V
29 ATT_INT    Output   Interrupt Attached Sensor, Active L    Interrupts        1.8V?
31 ATT_XSHUT  Input    Attached Sensor XSHUTDOWN                                    1.8V
33 Reserved (NC)         PWM Motor control


Towards image sensors

2  XSHUTDOWN  Input    Camera Reset, Active Low   
4  PWRDN      Input    Camera Power Down
6  CAM_SID    Input    Sensor slave address selection input   (tentative)
8  CAM_FSIN   I/IO     Frame sync input
10 EXTCLK      Input   External Clock Input
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


