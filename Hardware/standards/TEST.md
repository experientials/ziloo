## Testing Ziloo

### Testing Camera Modules with Compulab Carrier Board

Test setup

- [Compulab SB-UCM-iMX8PLUS](https://www.compulab.com/products/carrier-boards/sb-ucmimx8plus-carrier-board/) 
- Ziloo 909 bridge board
- 2 * 30 pins I-PEX cables
- 2 * Ziloo 201 camera modules
- HDMI display, Keyboard, Mouse

Test that

- Yocto Firmware boots with Linux Desktop
- Android Firmware boots with Linux Desktop


### Testing Camera Modules with Bridge Board

Test setup

- [SB-UCM-iMX8PLUS](https://www.compulab.com/products/computer-on-modules/ucm-imx8m-plus-nxp-i-mx-8m-plus-som-system-on-module-computer/)
- Ziloo 909 bridge board
- 2 * Ziloo 201 camera modules
- HDMI display via microHDMI
- USB 2.0 hub, Keyboard, Mouse via T-USB Host

Test that

- Verify that a 5V/1A USB-C power connector can boot up the board with cameras connected
- Run Stereo camera viewing app on the HDMI display
- 


### Testing USB Power and data of Bridge board

Test setup

- [SB-UCM-iMX8PLUS](https://www.compulab.com/products/computer-on-modules/ucm-imx8m-plus-nxp-i-mx-8m-plus-som-system-on-module-computer/)
- Ziloo 909 bridge board
- HDMI display via microHDMI
- USB 2.0 hub, Keyboard, Mouse via T-USB Host

Test that
- Yocto Firmware boots with Linux Desktop
- Android Firmware boots with Linux Desktop
- Board can boot with power via USB-C
- 


USB Power levels to test

- Dedicated Charger 5V, 500mA
- Apple Dedicated Charger 5V, 1A BC1.2
- Power & Data CDP 5V, 1A
- Power & Data CDP 5V, 3A
- Power & Data CDP 9V, 1A
- Power & Data CDP 15V, 1A


### Testing M.2 expansions of Bridge Board

- M.2 Key B+M NVMe SSD card
- M.2 Key A+E WiFi card (SDIO)
- [SB-UCM-iMX8PLUS](https://www.compulab.com/products/computer-on-modules/ucm-imx8m-plus-nxp-i-mx-8m-plus-som-system-on-module-computer/)
- Ziloo 909 bridge board
- HDMI display via microHDMI
- USB 2.0 hub, Keyboard, Mouse via T-USB Host


### Testing with HDMI Touch Display

- [SB-UCM-iMX8PLUS](https://www.compulab.com/products/computer-on-modules/ucm-imx8m-plus-nxp-i-mx-8m-plus-som-system-on-module-computer/)
- Ziloo 909 bridge board
- 2 * Ziloo 201 camera modules
- USB 2.0 hub, Keyboard, Mouse via T-USB Host
- [11.6 SMART TOUCH 11.6" Smart Touch Panel (HDMI Touch Solution)](https://www.twscreen.com/otherproduct/20966/11.6smarttouch/11.6/-Smart-Touch-Panel-(HDMI-Touch-Solution)) 


####

You should have the development board and 201 camera modules

- Test CSI connectors route signals and power
- Test USB connectors can power the board
- Test SoM can boot with HDMI, Mouse and Keyboard
- Test that the development board can be connected via 30 pin CSI connectors
- Test dual Rpi 22 pins camera connections -> 909b -> development board 
- Verify boot to USB/SD/eMMC
- Verify that small m.2 modules can be fitted
- Verify power delivery from USB chargers with the listed levels
- Document test process and findings

Deliverables:

- Report results and send the hardware(incl. Compulab dev board) back to me.
- All design files & send the hardware including test setup
