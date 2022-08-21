### M.2 Key E Pin allocations

| Pin id.	| Upper     | Lower      | Description                        | Counterpoint   | Voltage  |
|-----------|-----------|------------|------------------------------------|----------------|----------|
| 1         | GND       |		     | Ground    	                      |                |          |
| 2         |           | +3.3V	     | 3.3 V power supply from main board |  			   | 3.3V     |
| 3	        | USB D+    |            | USB data pair positive             | USB D+         | 		  |
| 4	        | 	        | +3.3V	     | 3.3 V power supply from main board |                | 3.3V     |
| 5	        | USB D-	|            | USB data pair negative	          | USB D-         |          |			
| 6	        | 	        | M2E_PWROFF | Card PWR OFF                       |	EX4.11   | 1.8/3.3  |
| 7	        | GND		|            | Ground                             |                | GND      |
| 8         |           | M2_I2S_CLK | GPIO5	M2_I2S_CLK                | SAI5_TXC       | 1.8V     |
| 9 	    | SDIO CLK  |            | SDIO	        		              | SD1 CLK        | 1.8V     |
| 10        |           | M2_I2S_WS  | GPIO8	M2_I2S_TXFS			      | SAI5_TXFS      | 1.8V     |
| 11 	    | SDIO CMD  |            | SDIO	        		              | SD1 CMD        | 1.8V     |
| 12	    |           | M2_I2S_TXD2| 	GPIO6	M2_I2S_DIN SAI5           | SAI5_TXD2      | 1.8V     |
| 13 	    | SDIO DATA0|            | SDIO	        		              | SD1 DATA0      | 1.8V     |
| 14	    |           | M2_I2S_RXD2|	GPIO7	M2_I2S_DOUT	SAI5	      | SAI5_RXD2      | 1.8V     |
| 15 	    | SDIO DATA1|            | SDIO	        		              | SD1 DATA1      | 1.8V     |
| 16	    |           | LED2#      | Add RXFS ?  	                      |                |          |
| 17 	    | SDIO DATA2|            | SDIO	        		              | SD1 DATA2      | 1.8V     |
| 18	    |    		| GND        | Ground                             |                | GND      |
| 19 	    | SDIO DATA3|            | SDIO	        		              | SD1 DATA3      | 1.8V     |
| 20        | 	        | UART WAKE# | Bluetooth uses to wake up platform | EX1.12         | 3.3V     |		
| 21        | SDIO WAKE#|            | WiFi uses to wake up platform      | EX1.13         | 1.8V     |		
| 22        |           | UART RxD   |                                    | UART2_RXD      | 1.8V     |
| 23        |SDIO RESET#|            | Signal to independently reset WiFi | SD1_RESET_B[?] | 1.8V     |
| 24 - 31   |			|            |                                    |                |          |   		
| 32        |           | UART TxD   |                                    | UART2_TXD      | 1.8V     |
| 33	    | GND		|            | Ground                             |                | GND	  |
| 34        |           | UART CTS   |                                    | UART4_RXD      | 1.8V     |
| 35        | PCIE TXN- |            | PCIE TXN- / PET-0 / SATA-A-        | -              | 1.8V     |			
| 36        |           | UART RTS   |                                    | UART4_TXD      | 1.8V     |
| 37        | PCIE TXN+	|            | PCIE TXN+ / PET-0 / SATA-A+        | -              | 1.8V     |			
| 38        |           | JTAG_TDO   | Debugging                          |                | 1.8V     |
| 39	    | GND		|            | Ground                             |                | GND	  |
| 40        |           | COEX4      | Wake up the WiFi                   | EX6.0          | 1.8V     |
| 41        | PCIE RXN-	|            | PCIE RXN- / PER-0 / SATA-B+        | -              |          |			
| 42        |           | DEV_BT_WAKE| Wake up the Bluetooth              | EX6.1[?]       | 1.8V     |
| 43        | PCIE RXN+ |            | PCIE RXN+ / PER+0 / SATA-B-        |	-              | 1.8V     |
| 44        |           | JTAG_TDI   | Debugging                          |                | 1.8V     |
| 45	    | GND		|            | Ground                             |                | GND      |
| 46        |           | JTAG_TCK   | Debugging                          |                | 1.8V     |
| 47        | PCIE REFCLK+ |         | PCIE REFCLK+				          | -              |          |
| 48        |           | JTAG_TMS   | Debugging                          |                | 1.8V     |
| 49        | PCIE REFCLK- |         | PCIE REFCLK-	                      | -              |          |
| 50        |           | SUSCLK     | 32.768 kHz provided by Platform    | -              |          |   			
| 51	    | GND		|            | Ground                             |                | GND	  |
| 52        |           | PERST0#    | PCI Reset	                      | -              |          |
| 53        | CLKREQ0#  | 	         | Reference clock request		      | -              | 3.3V     |
| 54        |           | W_DISABLE2#| Independently reset the Bluetooth  | EX1.10 EX4.9   | 1.8V     |
| 55        | PE WAKE#  |            | PCIe uses to wake up platform      | -              | 1.8V     |		
| 56        |           | W_DISABLE1#| Full power down Bluetooth + WiFi   | EX1.11 EX4.10  | 1.8V     |
| 57	    | GND		|            | Ground                             |                | GND	  |
| 58        |           | I2C_DATA   | I2C DATA                           | I2C3 SDA       | 1.8V     |
| 59        | USB3 TX+  |            | PET+1 / SSIC	M2_USB3_SSTX+		  | M2_USB3_SSTX+  |          |
| 60        |           | I2C_CLK    | I2C CLK                            | I2C3 SCL       | 1.8V     |
| 61        | USB3 TX-	|            | PET-1 / SSIC	M2_USB3_SSTX-	      | M2_USB3_SSTX-  |          |
| 62        |           | ALERT#     |                                    | EX1.7          | 1.8V     |
| 63	    | GND		|            | Ground                             |                | GND      |
| 64        |           | SWD CLK PD | SWD Clock Power                    | SWD CLK PD     |          |
| 65        | USB3 RX+  |            | PER+1 / SSIC	M2_USB3_SSRXP		  | M2_USB3_SSRX+  |          |	
| 66		|           | SWD DAT PD | SWD Data Power                     | SWD DAT PD     |          |
| 67	    | USB3 RX-	|            | PER-1 / SSIC	M2_USB3_SSRXN		  | M2_USB3_SSRX-  |          |	
| 68        |           | SWD CLK RP | SWD Clock RP		                  | SWD CLK RP     |          |
| 69	    | GND		|            | Ground                             |                | GND      |
| 70        |           | SWD DAT RP | SWD Data RP                        | SWD DAT RP     |          |
| 71        | RP UART   |            |                                    | UART_RP_RXD    | 3.3V     |
| 72        |           | VRES       | Power	VRES			          |                | +3.3V    |
| 73        | RP UART   |            |                                    | UART_RP_TXD    | 3.3V     |
| 74        | 	        | VRES       | Power	VRES			          |                | +3.3V    |
| 75	    | GND		|            | Ground                             |                | GND	  |


Supports

- WNFB-266XI SDIO Wireless Module via SoM (SD1, UART2)
- Debugging/Probe module
- [?] Consider Which I2C to default: I2C3 or I2C6
- [?] How to support I2S and PCM alternately
