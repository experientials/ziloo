# Surface mounted USB Charging PCB Design

I'm looking for a PCB design for a Lithium Power Module.

It consists of 3 boards. Two internally and one externally

1. [Bottom board](./BOTTOM_BOARD.md) which prove the Underside Connector Isles reflecting USB-C pins.
2. [Reverse Sibling board](./SIBLING_BOARD.md) which has the mirror of the Isles on the Bottom board and is external.
3. [Slide-in board](./SLIDE-IN_BOARD.md) which passes power and signals to the device via 12 compression pins.

You will,

* Design diagrams for the three boards
* Determine if internal 3.3V must be passed between bottom and slide-in boards to drive LED. 
  It could replace EXT_PWRON
* Review the chosen components
* Review ESD/ECM protection design
* Review the designs for future European compliance application
* Review suggestions with PO before finishing
* Make PCB designs for Bottom board & Reverse Sibling board
* List BoM
* Plan ways to quality test the board
* Consider design improvements towards assembly and production
* Produce a small test batch with PCBWay or JCLPCB (White 1mm)
* Optional/Future: Measure EMC emissions of the board at charge, discharge and USB data transfer
* Deliver test PCBs with mounted components & design files

It's all in a private GitHub repo. At the end I'd want to check design files into the repo.
I will want to have design files in addition to manufacturing files that can be used for future
revisions. They must be in a format(or alternate format) that can be revised by low cost software.

## Visual overview 

![Power Module](./Power_Module.jpg)
