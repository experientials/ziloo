? Event interrupts vs GPIO
? Timers
? Aux IMU I2C

| Pin | Pad      |                    | to        |  
|-----|----------|--------------------|-----------|
| 1   | M3SDA    | Left CSI1 I2C SDA  | SOM I2C5  |
| 2   | M3SCL    | Left CSI1 I2C SCL  | SOM I2C5  |
| 3   | HOSTBOOT | System Control     | EX0.6          |
| 4   | QSPI_D0  | Flash              | Flash chip          |
| 5   | QSPI_CLK | Flash              | Flash chip |
| 6   | VREG     | Supply             | 1.8V          |
| 7   | VDDIO    | Supply             | 1.8V ?          |
| 8   | QSPI_D3  | Flash              | Flash chip |
| 9   | RESETN   | System Control     | EX0.5       |
| 10  | HIRQ     | Host I2C IRQ       | SOM I2C3 / EX0  |
| 11  | HSDX     | Host I2C SDA       | SOM I2C3  |
| 12  | VDDIO    | Supply             |           |
| 13  | M2SCX    | Right CSI2 I2C SCL | SOM I2C6  |
| 14  | QSPI_CSN | Flash              | Flash chip |
| 15  | QSPI_D1  | Flash              | Flash chip |
| 16  | MCSB3    | GPIO / Chip Select 3 | Breakout |
| 17  | GND      | Supply             |        |
| 18  | MCSB2    | GPIO / Chip Select 2 | Breakout |
| 19  | MCSB4    | GPIO / Chip Select 4 | Breakout |
| 20  | QSPI_D2  | Flash              | Flash chip |
| 21  | OCSB     | IMU Auxiliary      | BMM150     |
| 22  | ASCX     | IMU Auxiliary      | BMM150     |
| 23  | JTAG_CLK | Debug               | Breakout  |
| 24  | JTAG_DIO | Debug               | Breakout  |
| 29  | M1SCX    | Master 1 I2C SCL  | Breakout |
| 30  | ASDX     | IMU Auxiliary      | BMM150     |
| 32  | HDSO     | I2C Address selector | LOW       |
| 33  | HSCX     | Host I2C SCL       | SOM I2C3  |
| 37  | M2SDI    | GPIO               | M2SDI |
| 38  | MCSB1    | GPIO / Chip Select 1 | Breakout |
| 39  | ASCX     | IMU Auxiliary      | BMM150     |
| 43  | M1SDI    | GPIO SPI Master 1  | Breakout |
| 44  | M1SDX    | Master 1 I2C SDA   | Breakout |

