# T-USB connector

The connector is a combination of two USB Type C connectors laid out in a T shape. They can be connected individually as USB Host and USB PC/Power (OTG), or by a combined connector. 

## Components

- 2 * [Hirose USB-C CX80B1-24P](https://www.hirose.com/product/p/CL0480-0625-0-00)
- 1 * TPS65982 USB Type-C® and USB PD Controller, Power Switch, and High-Speed Multiplexer
- 1 * HD3SS460 4 x 6 Channels USB Type-CTMAlternate Mode MUX. Connected to T-USB Host
- 2 * HD3SS3220  10-Gbps USB 3.1 Type-C 2:1 mux with DRP Controller
- USB to UART/I2C/SPI mux

## USB Host

The Host mode connector is the vertical stem of the T. 
The USB Host connector can be connected to a dedicated Control and Connectivity module. This module enables
software updates and configuration over Bluetooth via a Mobile App. It also manages awakeness and provides additional environment sensors. 
The USB 2.0 lines can connect to mouse and keyboard.
Alternately it can be used as a general USB 3.0 connection or as Display Port in alternate mode.
This is provided by converting LVDS to Display Port.
The connector can also supply 5V power to the board.


## USB PC/Power (OTG)

The OTG connector is the horizontal bar of the T.
Using OTG mode the connector can be used as a USB device.
The USB OTG connector allows you to use Ziloo as a traditional WebCam using a PC/Mac or Mobile Phone.
In alternate mode it provides 4 lanes of ethernet connectivity.
The connector can also supply 5V power to the board.

* LVDS / MIPI DSI
* [HDMI Alternate Mode for USB Type-C](https://en.wikipedia.org/wiki/HDMI#HDMI_Alternate_Mode_for_USB_Type-C) - [SuperUser info](https://superuser.com/a/1193853)


## Using T-USB Cable

When connecting with a dedicated cable the in-built resistors switches the connection to allow more signals.
The resistors are connected to CC pins to signal the T-USB Extended mode. 

The CC pins can be used to enable alternate T-USB cables for different connections such as,

In extended mode the DX lines provide two additions signals for UART2 & UART4 debug lines.
DX+ DX- pins are used for debugging connections. Re: Serial Debug console UART2 & 4.


TODO Scenarios

* USB 2.0 switching & debug chipset with debug breakout
* Power + Bluetooth/Controller + HDMI Display
* Power + Webcam
* Power + Bluetooth/Controller + Ethernet
* Power + Bluetooth/Controller + Ethernet + HDMI Display


TODO Visual diagram


* Ethernet RX/TX  (4 pins)
* HDMI RX/TX (4 pins)
* Sensor I3C / I2C for Cameras/ToF
* [UG233: USB Type-C Reference Design User's Guide](./datasheets/UG233-USB-Design-Guide.pdf)
* [USB-CTM to DisplayPort Active Cable Reference Design](./datasheets/tidudr0.pdf)
* [Alternate Mode for USB Type-CTM: Going beyond USB](./datasheets/slly021.pdf)
* [STEVAL-USBC2DP USB Type-CTM to DisplayPortTM adapter](./datasheets/dm00474479-stevalusbc2dp-usb-typec-to-displayport-adapter-stmicroelectronics.pdf)


From 5.2.1

External regulator control and power management
UCM-iMX8M-Plus supports carrier board power supply control by means of two dedicated output signals. Both signals are derived from the i.MX8M Plus SoC. The logic that controls both signals is supplied by the i.MX8M Plus SoC SNVS power rail.
The PMIC_STBY_REQ output can be used to signal the carrier board power supply that UCM- iMX8M-Plus is in ‘standby’ or ‘OFF’ mode. Utilizing the external regulator control signals enables carrier board power management functionality.
Please refer to the i.MX8M Plus Reference manual for additional details. The table below summarizes the external regulator control signals.
Table 38 External regulator control signals
     Signal Name
PMIC_STBY_REQ PMIC_ON_REQ PWRBTN
5.3 Reset
Pin # Type
P1-66 O P1-68 O P2-64 I
Description
When the processor enters SUSPEND mode, it will assert this signal.
Active high power-up request output from i.MX8M Plus SoC.
Pulled-Up Active low ON/OFF signal (designed for an ONOFF switch).
Availability
Always available Always available Always available
                    SYS_RST_PMIC signal is the main system reset input. Driving a valid logic zero invokes a global reset that affects every module on UCM-iMX8M-Plus. Please refer to the i.MX8M Plus Reference manual for additional details.
Table 39 Reset signals
Signal Name Pin # Type Description
SYS_RST_PMIC P1-2 I Active Low cold reset input signal. Should be used as main system reset

Availability
Always available





### DF40 60 pin connector

EXTRA height ?


Toward thin part with microphone and other sensors

| Pin | Code       | Type     | Details                              | Voltage |
|-----|------------|----------|--------------------------------------|---------|
| 1   | USB1_VBUS  | Power    | USB1 Bus power                       |         |
| 2   | GND        | Power    | Ground                               |         |
| 3   | USB1_DP    | USB      | USB1 D+                              |         |
| 4   | USB1_DN    | USB      | USB1 D-                              |         |
| 5   | USB1_RX_DP | USB      | USB1 RX D+                           |         |
| 6   | USB1_RX_DN | USB      | USB1 RX D-                           |         |
| 7   | GND        | Power    | Ground                               |         |
| 8   | USB1_TX_DP | USB      | USB1 TX D+                           |         |
| 9   | USB1_TX_DN | USB      | USB1 TX D-                           |         |
| 10  | GND        | Power    | Ground                               |         |
| 11  | TRCLK+     | Network  | ETH0 TR CLK+                         |         |
| 12  | TRCLK-     | Network  | ETH0 TR CLK-                         |         |
| 13  | GND        | Power    | Ground                               |         |
| 14  | TR1+       | Network  | ETH0 TR 1+                           |         |
| 15  | TR1-       | Network  | ETH0 TR 1-                           |         |
| 16  | GND        | Power    | Ground                               |         |
| 17  | TR2+       | Network  | ETH0 TR 2+                           |         |
| 18  | TR2-       | Network  | ETH0 TR 2-                           |         |
| 19  | GND        | Power    | Ground                               |         |
| 20  | TR3+       | Network  | ETH0 TR 3+                           |         |
| 21  | TR3-       | Network  | ETH0 TR 3-                           |         |
| 22  | GND        | Power    | Ground                               |         |
| 23  | TR4+       | Network  | ETH0 TR 4+                           |         |
| 24  | TR4-       | Network  | ETH0 TR 4-                           |         |
| 25  | GND        | Power    | Ground                               |         |
| 26  | LED_ACT    | Network  | ETH0_LED_ACT                         |         |
| 27  | LED_10_100 | Network  | ETH0_LINK-LED_10_100                 |         |

| 1   | SYS_RST_PMIC | Reset  | Power Management SYS Reset           |         |

USB1_TCPC_nINT
ALT_BOOT
PMIC_STBY_REQ
PMIC_ON_REQ
POR_B_3P3

| 24  | GND        |                                          |
| 40  | TOUCH_INT  | LVDS TOUCH INT EX0.6                   |
| 41  | TOUCH_RST  | LVDS TOUCH Reset EX0.7                   |



Reduce ETH0 to RX/TX








Towards image sensors

| Pin | Code       | Type     | Details                              | Voltage |
|-----|------------|----------|--------------------------------------|---------|
| 60  | USB2_VBUS  | Power    | USB2 Bus power                       |         |
| 59  | GND        | Power    | Ground                               |         |
| 58  | USB2_DP    | USB      | USB2 D+                              |         |
| 57  | USB2_DN    | USB      | USB2 D-                              |         |
| 56  | USB2_RX_DP | USB      | USB2 RX D+                           |         |
| 55  | USB2_RX_DN | USB      | USB2 RX D-                           |         |
| 54  | GND        | Power    | Ground                               |         |
| 53  | LVCLK+     | LVDS     | LVDS CLK+                            |         |
| 52  | LVCLK-     | LVDS     | LVDS CLK-                            |         |
| 51  | GND        | Power    | Ground                               |         |
| 50  | LVD0+      | LVDS     | LVDS D0+                             |         |
| 49  | LVD0-      | LVDS     | LVDS D0-                             |         |
| 48  | GND        | Power    | Ground                               |         |
| 47  | LVD1+      | LVDS     | LVDS D1+                             |         |
| 46  | LVD1-      | LVDS     | LVDS D1-                             |         |
| 45  | GND        | Power    | Ground                               |         |
| 44  | LVD2+      | LVDS     | LVDS D2+                             |         |
| 43  | LVD2-      | LVDS     | LVDS D2-                             |         |
| 42  | GND        | Power    | Ground                               |         |
| 41  | LVD3+      | LVDS     | LVDS D3+                             |         |
| 40  | LVD3-      | LVDS     | LVDS D3-                             |         |
| 39  | GND        | Power    | Ground                               |         |

| 50  | UART1_TXD  | UART     | P1.72 UART1 Tx                       |         |
| 49  | UART1_RXD  | UART     | P1.19 UART1 Rx                       |         |
| 48  | UART2_TXD  | UART     | UART2 Tx                             |         |
| 47  | UART2_RXD  | UART     | UART2 Rx                             |         |
| 46  | UART3_TXD  | UART     | P1.61 UART3 Tx                       |         |
| 45  | UART3_RXD  | UART     | P1.21 UART3 Rx                       |         |
| 44  | UART4_TXD  | UART     | UART4 Tx                             |         |
| 43  | UART4_RXD  | UART     | UART4 Rx                             |         |
| 42  | I2C SCL    | I2C      | P1.99 SYS SCL                        |         |
| 41  | I2C SDA    | I2C      | P1.97 SYS SDA                        |         |
| 40  | I2C3 SCL   | I2C      | Stem SCL                             |         |
| 39  | I2C3 SDA   | I2C      | Stem SDA                             |         |


| 31  | Reserved   |          |                                      |         |
| 30  | Reserved   |          |                                      |         |



