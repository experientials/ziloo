# 801 T-USB daughterboard Upwork task

The T-USB daughterboard has two functions
- Supply the system with power
- Support smart future waking/suspend logic
- Provide data signals in the system over two USB-C connectors

The T-USB board exposes two vertical USB-C sockets and connects to the carrier board through two 50 pin B2B connectors.
For future feature development the board also has two FPC breakout connectors.

In addition to this board a matching **testing/breakout board must be designed**.

We already have a development board designed so this tasks breaks out part of an existing design (909) on a dedicated baord (801 T-USB).

The provided documentation includes

- Detailed functionality, wiring, connections for T-USB board
- Detailed functionality, wiring, connections for TESTING board
- Functionality Testing cases
- Reference diagram for Compulab development board
- Reference diagram for 909 development board
- Component datasheets

![Ziloo 801 T-USB Board](./T-USB-board.png)

![Ziloo 801 T-USB Board](./ziloo-801-T-USB-test.png)


The board takes two USB-C connections with power and data.

- Supports 5V in and out
- USB 2.0/3.0 data support
- Rudimentary Alt. Mode support
- Trickle charging & Fast Charging
- With/Without Battery connected
- Steady power output regardless of charging
- Power output max. 4.5V 2.5A


The essential BOM of the 801 T-USB Bridge Board is,

- 2 * [Hirose DF40-50DP-0.4V](https://www.hirose.com/en/product/p/CL0684-4014-0-51)
- 2 * [Hirose USB-C CX80B1-24P](https://www.hirose.com/product/p/CL0480-0625-0-00)
- 1 * [TPS65988](https://www.ti.com/product/TPS65988?keyMatch=TPS65988&tisearch=search-everything&usecase=GPN) Dual Port USB Type-C® and USB PD Controller, Power Switch, and High-Speed Multiplexer. 
- 2 * [HD3SS460](https://www.ti.com/product/HD3SS460?keyMatch=HD3SS460&tisearch=search-everything&usecase=GPN) 4 x 6 Channels USB Type-C Alternate Mode MUX. Connected to T-USB Host. 
- 1 * PCA9555 I/O Expander
- 4 * [TS5USBC410 Dual 2:1 USB 2.0 Mux/DeMux Switch](../datasheets/USB/ts5usbc41.pdf). [Mouser](https://www.mouser.ch/ProductDetail/Texas-Instruments/TS5USBC410IYFFR?qs=sGAEpiMZZMutXGli8Ay4kPB6XEQFysSpdNErqZgdEYs%3D)
- 1 * [BQ24250RGER battery charger](https://www.ti.com/product/BQ24250)  
- 1 * [3 pin JST SH socket SM03B-SRSS-TB](https://www.jst-mfg.com/product/detail_e.php?series=231) 
- 2 * [TE Connectivity 45PIN 0.3MM 571-4-2328724-5 FPC 3-2328724-5](https://www.te.com/usa-en/product-4-2328724-5.html)


Test board components,

- 2 * [Hirose DF40-50DS-0.4V](https://www.hirose.com/en/product/p/CL0684-4009-0-51) mated height 1.5mm
- 2 * [HD3SS3220  10-Gbps USB 3.1 Type-C 2:1 mux with DRP Controller](https://www.ti.com/product/HD3SS3220)
- 2 * USB-C connectors [DX07S024JA1R1300](https://www.jae.com/en/connectors/series/detail/product/id=66508) or [DX07S024JJ2R1300](https://www.mouser.ch/ProductDetail/JAE-Electronics/DX07S024JJ2R1300?qs=odmYgEirbwyfyaz1Tta0cQ%3D%3D)
- 3 * [Samtec TSW-116-14-T-S Header 16 pin](https://www.samtec.com/products/tsw-116-14-t-s)



## Milestones:

The project is broken down in milestones to ensure a correct design.

### Testing board design $300

Do a design for the testing board and layout with Eagle or Altium

- Precise placement of USB-C socket holes
- Preciese placement of upper and under 50 pin connectors
- Breakout connectors can be arranged differently
- USB breakout connectors should be as suggested
- The breakout part of the board can be enlarged if needed

Once the design is done we will order a few boards for me and yourself for testing.


### Initial board designs  $800

Do an initial board diagram and layout with Eagle or Altium.

- Confirmation of BoM
- PD Controller working as a power sink(not source)
- Power Regulators
- Power LED, Power and Reset buttons
- 45 pin breakout connectors
- USB-C sockets
- Battery charger
- Design both boards

Deliverables:

- Diagrams(.sch) + Board layout design files
- Gerber files
- Review the choice of component and suggest alternative if needed.
- Confirmation of BoM
- Get production quotes with JLCPCB, PCBWAY etc. for 10pc, 100pcs, 1000pcs (assembled and basic)


### Ordering test batch of boards $0

We then do a test batch of 801 T-USB boards


### Verification of design and fixes - $400

Receive the test boards and test the acceptance tests. Make sure all tests pass.
Correct any issues after reviewing with me.

Deliverables:

- Diagrams(.sch) + Board layout design files
- Gerber files
- Testing report with measurements
