# Autonomous Awareness

The Autonomous Awareness is distributed across systems some in the Occi some in the Stem.
The canonical implementation uses RP2040 to communicate and monitor sensors.

Occi Subcognition runs on the System Module by occasionally waking up to check the
camera sensors against the previous state.

Stem Awareness is an Autonomous system that runs at all time by reacting to
sensor changes when they happen.

- T-USB Stem MCU
- RT MCU on SoM
- MCU on m.2
- Bluetooth enabled nRF MCU

:[Inter MCU](../../Hardware/standards/INTER_MCU_BUS.md)
