# Activity Device

The Activity device driver constantly monitors to combine the state of 3 sensors

- APDS-9960 Proximity Light and Gesture Sensor
- VM3011 Multi-mode microphone
- MC6470 Motion Sensor

Time since:
- Any activity
- Sound above Background
- Room light switched on
- Ambient light changed above global absolute threshold (darkness)
- Ambient light changed below global absolute threshold (daylight)
- Self moved

It should be possible to access the device events by creating ISR/interrupt handler in any language (Python/Rust/C).
The handler would be called on new activity. Once an activity is registered the same should not be triggered again within 100ms.

Activity:
- Ambient light changed above a global diff threshold
- Ambient light movement in a direction
- Ambient color change
- 3D movement direction changed (self)
- Rotated (self)
- Dropped (self)
- Speaking started
- Music started
- Speaking stopped
- Music stopped

Config
- Darkness threshold (night time/dark room)
- Light needed for good camera input
- Bright light
- Light resolution that is considered a change
