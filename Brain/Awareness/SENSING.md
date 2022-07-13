# Autonomous Sensing

The system is constantly sensing the environment regardless of wakefullness.
Multiple sensors are used and connected to interrupts via I/O Extender 3.

Sensor Types
- Accelerometer (MC6470)
- Gyroscope (MC6470)
- Magnometer (MC6470)
- Ambient Light APDS-9960
- Human Body Interference (Analog)
- Microphone
- NFC

Each sensor has a Rust embedded-hal device driver to arrange the communication.



### Sensing Events

The MCU waits for events to happen, triggered via interrupt requests, 
and then records them updating the event log and world state.

(?) Which events to expect from MC6470

- Acceleration changed
- Orientation changed
- Device moved
- Ambient light change
- Body present/absent
- Human voice
- NFC Event



### Events and Interpretation

Recent events are interpreted to meta events such as,

- Shaking
- Vibrating
- Dropped
- Thrown
- Waving in sight
- Moving past left
- Moving past right


### World state

The Autonomus MCU attempts to maintain a 3D Spatial Self Location and Orientation of Occi Vision.

- Starting Location and Orientation is 0,0,0 and 0,0,0
- Location and Orientation is relative to when the system started
- When MCU resets the estimated Location and Orientation is marked
- Mark points that save the Location and Orientation at time stamp
- Sensor events update of Location and Orientation
- If a transport period(packed away/moving fast) is detected a mark is made at end of transport
- 

The Autonomous MCU keeps track of the current Ambient Light state
