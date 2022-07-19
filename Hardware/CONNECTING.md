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

When the i.MX SoM is in recovery mode `mfgtool` can be used to directly upgrade the firmware(in eMMC).


## Connection modes

You can connect USB cables to Ziloo in different ways depending on your needs. Normally you would connect your Computer or iPad to the OTG socket(the horizontal bar of the T) and devices such as a Display, keyboard or mouse to Host(the vertical bar of the T). It you plug **Ziloo** into **The Stand**
it will use the Plural mode where additional connections are available.

T-USB OTG 2.0 data,
- off (Autonomous MCU USB talks to Occi MCU USB1)
- Autonomous MCU USB (A and B)
- Occi MCU USB1 (only B)
- Plural; OTG-A connects Autonomous MCU USB, OTG-B connects Extra OTG USB

T-USB Host 2.0 data,
- off
- Autonomous MCU USB
- Occi MCU USB2 (only B)
- Plural; Host-A connects Autonomous MCU USB, Host-B connects Extra Host USB

T-USB OTG 3.0 data,
- off
- Occi MCU USB1
- Ox- / Ox+

T-USB Host 3.0 data,
- off
- Occi MCU USB2
- Hx- / Hx+


Host
- Plugging in a USB stick to update Ziloo

OTG
- MSC uploading firmware


## Future Connectivity Options

tcp/ip
bluetooth comms


### BLE Protocol Design Strategy

[Bluetooth Low Energy Serial: A Valid Design Strategy?](https://punchthrough.com/serial-over-ble/)

* Start with a Serial over BLE strategy and extract functionality as needed.
* Any value that will need to be accessed quickly by the central should have a readable characteristic that the peripheral always keeps up to date.
* Bulk background transfers, such as logs or firmware updates, should have their own characteristics, so they don’t clog up communication related to the user experience.
* Status information that changes quickly should be grouped so that the information can be considered a snapshot of a single point in time. This is extremely useful when working with systems where data from multiple kinds of sensors is needed to describe the device’s status.
* Information that is not of use to the current client should be transferred through a different characteristic or should have the ability for the client to turn the information on or off based on its interests. This way, the client can control what information it receives.
* Information that can be of value to other systems should be exposed through standard Bluetooth Profiles. (Information such as battery level, temperature, etc.).


### Command Line Sample Code

* [Command Line Interface library](https://infocenter.nordicsemi.com/topic/com.nordic.infocenter.sdk5.v15.2.0/lib_cli.html)

* [Command Line Interface (CLI) Example](https://infocenter.nordicsemi.com/topic/com.nordic.infocenter.sdk5.v15.2.0/cli_example.html)

https://infocenter.nordicsemi.com/index.jsp?topic=%2Fcom.nordic.infocenter.sdk5.v15.2.0%2Flib_cli.html&cp=4_0_0_3_10


### USB Mass Storage and Sound Streaming

* [usb-cdc-acm](https://github.com/NordicPlayground/node-usb-cdc-acm)
* [USB CDC ACM Example](https://infocenter.nordicsemi.com/topic/com.nordic.infocenter.sdk5.v15.2.0/usbd_cdc_acm_example.html)


### WebUSB

[WebUSB ChromeStatus](https://www.chromestatus.com/feature/5651917954875392)

[Web IDL](https://heycam.github.io/webidl/#idl-octet)


### Sample code

* [UART Example](https://infocenter.nordicsemi.com/index.jsp?topic=%2Fcom.nordic.infocenter.sdk5.v15.0.0%2Fuart_example.html)
* [Experimental: BLE Interactive Command Line Interface Example](https://infocenter.nordicsemi.com/topic/com.nordic.infocenter.sdk5.v15.0.0/ble_sdk_app_interactive.html)
* [Programming SoftDevices](https://infocenter.nordicsemi.com/index.jsp?topic=%2Fcom.nordic.infocenter.sdk5.v15.0.0%2Fgetting_started_softdevice.html&anchor=getting_started_sd)
* [ble_nus_init_t Struct Reference](https://infocenter.nordicsemi.com/index.jsp?topic=%2Fcom.nordic.infocenter.sdk5.v14.0.0%2Fble_sdk_app_nus_eval.html)

