# The Stem

The Stem connects various parts,

- SoM M7
- Faceboard Expander ([Stem Expander](./STEM-EXPANDER.md))
- T-USB Expander ([Stem Expander](./STEM-EXPANDER.md))
- M.2 Supervisor Card MCU
- Attached Integrated Testing Raspberry Pi
- Directly attached sensors

The directly attached sensors must be managed by the MCU that is currently mastering the bus.

- MC6470 Motion Sensor
- IS31FL3730 LED Matrix
- Faceboard EEPROM
- BQ24250 LiPO Battery Charger
- TPS65988 PD Controller

These sensors will trigger interrupt on STEM_INT. 
