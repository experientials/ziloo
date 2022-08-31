##### Mating Connectors

| Ref.     | UCM-iMX8M-Plus connector   | UCM-iMX8M-Plus socket  |
|----------|----------------------------|-----------------------|
| P1, P2   | Hirose DF40C-100DP-0.4V51  | DF40HC(3.0)-100DS-0.4V(51) |

| Ref.     | T-USB connector            | T-USB socket              |
|----------|----------------------------|---------------------------|
| P1, P2   | Hirose DF40C-50DP-0.4V51   | DF40HC(3.0)-50DS-0.4V(51) |

TODO Stereo Camera module


##### Mechanical Drawings

UCM-iMX8M-Plus top

![UCM-iMX8M-Plus top](../refs/Compulab/UCM-iMX8M-top.png)

UCM-iMX8M-Plus bottom

![UCM-iMX8M-Plus top](../refs/Compulab/UCM-iMX8M-bottom.png)


1. All dimensions are in millimeters.
2. The height of all components is < 2.0mm.
3. Baseboard connectors provide 3 ± 0.15mm board-to-board clearance.
4. Board thickness is 1.6mm.

3D model and mechanical drawings in DXF format are available at https://www.compulab.com/products/computer-on-modules/UCM-iMX8M-Plus-nxp-i-mx-8m- mini-som-system-on-module-computer/#devres


T-USB 801 board dimensions 33 mm x 24 mm

Clearance height below the T-USB

High socket, leaving camera below or above?


##### APPLICATION NOTES from  UCM-iMX8M-Plus Reference guide.

- Ensure that all V_SOM and GND power pins are connected.
- Major power rails - V_SOM and GND must be implemented by planes, rather than traces. Using at least two planes is essential to ensure the system signal quality because the planes provide a current return path for all interface signals.
- It is recommended to put several 10/100uF capacitors between V_SOM and GND near the mating connectors.
- Except for a power connection, no other connection is mandatory for UCM-iMX8M-Plus operation. All power-up circuitry and all required pullups/pulldowns are available onboard UCM-iMX8M-Plus.
- If for some reason you decide to place an external pullup or pulldown resistor on a certain signal (for example - on the GPIOs), first check the documentation of that signal provided in this manual. Certain signals have on-board pullup/pulldown resistors required for proper initialization. Overriding their values by external components will disable board operation. For details please refer to section Error! Reference source not found..
- You must be familiar with signal interconnection design rules. There are many sensitive groups of signals. For example:
- PCIe, Ethernet, USB and more signals must be routed in differential pairs and by a controlled impedance trace.
- Audio input must be decoupled from possible sources of carrier board noise.
- The following interfaces should meet the differential impedance requirements with
manufacturer tolerance of 10%:
- USB2.0: DP/DM signals require 90 ohm differential impedance.
- All single-ended signals require 50 ohm impedance.
- PCIe TX/RX data pairs and PCIe clocks require 85 ohm differential impedance.
- Ethernet, MIPI-CSI and MIPI-DSI signals require 100 ohm differential impedance.
- The carrier board interface connectors provide 3mm mating height. Bear in mind that there are components on the bottom side of UCM-iMX8M-Plus. It is not recommended to place any components underneath the UCM-iMX8M-Plus module.
- Refer to the SB-UCMIMX8PLUS carrier board reference design schematics.
- It is recommended to send the schematics of the custom carrier board to Compulab
support team for review.

V_SOM is recommended between 3.45 and 4.4 volt, typical 3.7

for more information see [UCM i.MX8 PLUS Reference Guide](../datasheets/i.MX8/ucm-imx8plus_reference-guide_2021-11-02.pdf)



##### Connecting the SB-UCM-iMX8PLUS carrier board

![SB-UCM-iMX8PLUS Carrier Board](../refs/Compulab/SB-UCMIMX8PLUS-carrier-board.jpg)

For further details see [Product Page](https://www.compulab.com/products/carrier-boards/sb-ucmimx8plus-carrier-board/#diagram).

- 2 * I-PEX connector directly between UCM carrier board and bridge board
- 45 pins connected to Inbetween breakout boards
- 10 pins power connector to Inbetween breakout boards
- USB-C connector to Inbetween breakout boards
- USB-A connector to Inbetween breakout boards
- HDMI female to Inbetween breakout boards

