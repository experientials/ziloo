# Camera CSI Connectors

### CSI connectors

The CSI connectors data lanes are connected directly together for each side. It is only possible 
to connect a single left and a single right camera module at a time.

The 22 pin and 30 pin CSI connectors are intended to be used without a daughter board and instead a separate i.MX8 development board is used.
The CSI lanes on 34 pins connector is connected directly to the equivalent lines on the 30 pins.
This assumes that a camera is connected to either a 34 pins connector or a 22 pins connector, not both.
If a i.MX8 daughter board is used rather than development board the CSI lines from the daughter board must
be connected to the 34 pin camera module connectors.
i.MX8 CSI1 is used for left module, CSI2 is used for right module.

The two 34 pin CSI connectors are wired to run in sync via the STROBE pin.

If power isn't connected over the USB-C plugs, the camera modules should be powered over the MIPI CSI connectors.
In this case it should be possible to use either the 22 pin connectors or the 30 pin connectors for inputting
the signal and power. This means that the 22 pin connectors can be used to input or output MIPI CSI lanes.

Signals on the 34 pins connector are 1V8.
SCCB for CSI1 is connected to I2C5 voltage shifted.
SCCB for CSI2 is connected to I2C6 voltage shifted.


### Power supply Camera Module

Power can be supplied from VSOM stepped down to 3V3, 2V8 and 1V8.
2V8 is only needed for the camera modules.

The 909 board can be used to test camera modules without any other module attached by using the
22 pins and 30 pins connectors.
If a T-USB Power Module isn't connected, so VSOM isn't supplied, the power has to come from 
the 30 pins and 22 pins CSI connectors. 


# Camera Connectors

## RPI FPC 22 pins

On the left(CSI1) side.

:[22 pins RPi CSI connector](../pinouts/RPI_22_CONNECTOR.md)


## NVIDIA FPC 30 pins

On the right(CSI2) side.

:[30 pins I-PEX CSI connector](../pinouts/I-PEX_30_CONNECTOR.md)


## Ziloo Camera Module 34 pin connector

**Just to be clear**: All CSI lanes are laid out on one side of the connector with GND between.

:[Camera Module 201 connector](../pinouts/CAMERA_MODULE_CONNECTOR_PINOUT.md)

