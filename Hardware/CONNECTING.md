# Connecting to iPad or PC

You can connect to Ziloo by plugging into the OTG part of T-USB

The OTG connector is the horizontal bar of the T.
Using OTG mode the connector can be used as a USB device.
The USB OTG connector allows you to use Ziloo as a traditional WebCam using a PC/Mac or Mobile Phone.

When connected the computer may power and/or charge Ziloo. If Ziloo has sufficient power it will wake up.

When awake multiple features will be active

- Ziloo will provide a stereo WebCam UVC stream.
- Ziloo will connect via CDC Ethernet to gain internet access. It will use this to update subscribed streams and firmware.
- UARTS 1 to 4 for debugging over CDC Virtual COM ports
- MSC access to SOM flash

When resting as well as awake the Ziloo stem provides basic features over USB 2.0

- I2C sensor access compatible with https://github.com/harbaum/I2C-Tiny-USB#i2c-tiny-usb
- command console interface via CDC Virtual COM port
- console output via CDC Virtual COM port
- MSC to upload python script runs

## console output

The console output will show output from both SoM cores and the RP applications. It will use ANSI to syntax highlight and show status/progress information. The status is encoded in the log and can be decoded by the Ziloo apps console view.


## command console

The command port connection provides a bidirectional structured command interface following a simple command-response sequence with async/out of order support. The command interface can be viewed and manipulated via the Ziloo App command view or VS Code plugin.


## UART ports

Ziloo will provide virtual ports named UARTx that connect to the SoM. If the SoM suspends the port remains open but unresponsive. The change will be logged in the console.


## I2C direct sensor

Sensors can be directly probed and tested from remote apps using drivers compatible with
[I2C tiny USB](https://github.com/harbaum/I2C-Tiny-USB#i2c-tiny-usb). This feature will not be available initially as it will need to be secured well. 
The same functionality could be provided via command port.


## Recovery features

If the RP fails to boot from the flash it enters recovery. Alternatively press the recovery button to enter.

Start with your Pico unplugged from USB. Hold down the BOOTSEL button, and while continuing to hold it (don’t let go!), plug the Pico into USB. Continue to hold the BOOTSEL button until the RPI-RP2 drive appears!

When in recovery mode an MSC disk is provided over USB 2.0 for updating the firmware.

- Replacing RP firmware
- Adding to system stream
- Adding to other streams
- Manipulate streams


Hard reset 