### M.2 Key B Pin allocations

| Pin id.	| Upper     | Lower      | Description                        | Counterpoint   | Voltage Level |
|-----------|-----------|------------|------------------------------------|----------------|---------------|
| 1         | CONFIG_3  |		     | Defines Module Type	              | pad            |               |
| 2         |           | +3.3V	     | 3.3 V power supply from main board |  			   | 3.3V          |
| 3	        | GND		|            | Ground	                          |                |  GND		|
| 4	        | 	        | +3.3V	     | 3.3 V power supply from main board |                | 3.3V          |
| 5	        | GND		|            | Ground (available?)                |                | GND	|
| 6	        | 	        | M2B_PWROFF | Card PWR OFF                       |	EX2.5          | 1.8/3.3   |
| 7	        | USB D+	|            | USB data pair positive	USB D+    | USB D+         |     |			
| 8	        | 	        | W_DIS1     | Wireless disable 1				  | EXB.3          |               |
| 9	        | USB D-	|            | USB data pair negative	USB D-    | USB D-         |     |			
| 10        | 	        | DAS/DSS	 | Device Actvty Signal               | LED / EX2.9    |		3.3V |
| 11	    | GND		|            | Ground (available?)	              |                | GND          |
| 12 - 19   |			|            |                                    |                |            |   		
| 20        |           | M2_I2S_CLK | GPIO5	M2_I2S_CLK                | MIC I2S        | 1.8V          |
| 21	    | CONFIG_0	|            |		  			                  | pad            |    |
| 22	    |           | M2_I2S_DIN | 	GPIO6	M2_I2S_DIN                | MIC I2S DATA0  | 1.8V         |
| 23	    | GPIO11    |            | 			NC			              | MIC I2S MCLK   | 1.8V         |
| 24	    |           | M2_I2S_DOUT|	GPIO7	M2_I2S_DOUT			      | SPK I2S DATA0  | 1.8V         |
| 25        | DPR       | 	         |   			                      | pad            |              |
| 26	    |           | GPIO10     | 	  			                      | EX2.10         | 1.8V         |
| 27	    | GND		|            | Ground	                          |                | GND          |
| 28        |           | M2_I2S_WS  | GPIO8	M2_I2S_WS			      | MIC I2S WS     | 1.8V         |
| 29	    | USB3 RX-	|            | PER-1 / SSIC	M2_USB3_SSRXN		  | M2_USB3_SSRX-  |              |	
| 30	    |           | SIM_RST    | UIM RESET			              | -              |              |
| 31        | USB3 RX+  |            | PER+1 / SSIC	M2_USB3_SSRXP		  | M2_USB3_SSRX+  |              |	
| 32		|           | SIM_CLK    | UIM CLK			                  | -              |              |
| 33        | GND		|            | Ground                             |                | GND	      |
| 34		|           | SIM_DATA	 | UIM DATA			                  | -              |              |
| 35        | USB3 TX-	|            | PET-1 / SSIC	M2_USB3_SSTX-	      | M2_USB3_SSTX-  |              |
| 36        |           | SIM_PWR    | UIM PWR			                  | -              |              |
| 37        | USB3 TX+  |            | PET+2 / SSIC	M2_USB3_SSTX+		  | M2_USB3_SSTX+  |              |
| 38        | 	        | DEVSLP     | Device Sleep, input. high=sleep    | EX2.12          | 3.3V         |	
| 39        | GND       |            | Ground	                          |                | GND          |
| 40        | 	        | M2 SMB SCL | SMB_CLK	M2 SMB SCL                | I2C3 SCL       | 1.8V         |
| 41        | PCIE RXN-	|            | PCIE RXN- / PER-0 / SATA-B+        | PCIE RXN-      |          |			
| 42        | 	        | M2 SMB SDA | SMB_DATA	M2 SMB SDA		          | I2C3 SDA       | 1.8V         |
| 43        | PCIE RXN+ |            | PCIE RXN+ / PER+0 / SATA-B-        |	PCIE RXN+      | 1.8V          |
| 44        | 	        | GPIO2      | GPIO2 / ALERT                      | EX2.7         | 1.8V          |
| 45        | GND		|            | Ground	                          |                | GND           |
| 46        | 	        | GPIO3      |   	                              | PWM2_OUT       | 1.8V          |
| 47        | PCIE TXN- |            | PCIE TXN- / PET-0 / SATA-A-        | PCIE TXN-      | 1.8V      |			
| 48        | 	        | GPIO4      | 	                                  | PWM3_OUT       | 1.8V          |
| 49        | PCIE TXN+	|            | PCIE TXN+ / PET-0 / SATA-A+        | PCIE TXN+      | 1.8V      |			
| 50        |           | PERST	     | PCI Reset	                      | mPCIe_PERST    |               |
| 51        | GND		|            | Ground                             |                | GND           |
| 52        | 	        | CLKREQ     | Reference clock request		      | PCIE_CLKREQ_B  | 3.3V         |
| 53        | PCIE REFCLK- |         | PCIE REFCLK-	                      | REFCLK-       |              |
| 54        | 	        | WAKE       | PCIe WAKE# Active Low.	          | PCIE_WAKE_B   |              |		
| 55        | PCIE REFCLK+ |         | PCIE REFCLK+				          | REFCLK+       |              |
| 56        | 	        | MFG_DAT    | SDA		                          | SYS I2C SDA   |               |	
| 57        | GND		|            | Ground                             |               |               |
| 58        | 	        | MFG_CLK    | SCL                                | SYS I2C SCL   |               |
| 59        | ANTCTL0   |            |                                    | ECSPI2_MISO   |               |
| 60        | 	        | COEX3      |                                    | MIC I2S DATA3  |               |
| 61        | ANTCTL1   |            |                                    | ECSPI2_SS0     |               |
| 62        | 	        | COEX_TXD   |   	                              | MIC I2S DATA2  | 1.8V          |
| 63        | ANTCTL2   |            |                                    | ECSPI2_SCLK    |               |
| 64        | 	        | COEX_RXD   |                                    | MIC I2S DATA1  | 1.8V          |
| 65        | ANTCTL3   |            |                                    | ECSPI2_MOSI    |               |
| 66        | 	        | SIM DETECT | SIM CD		                      | -              |               |
| 67        | RESET#	|            | RESET			                  | EX2.6          |  1.8V         |
| 68        |           | SUSCLK     | 32.768 kHz provided by Platform    | -              |  |   			
| 69        | CONFIG_1	|            | Defines module type			+	  | EX2.14          |               |
| 70        |           | VRES       | Power	VRES			          |               | +3.3V         |
| 71        | GND		|            | Ground				              |               | GND           |
| 72        |           | VRES       | Power	VRES			          |               | +3.3V         |
| 73        | GND		|            | Ground				              |               | GND           |
| 74        | 	        | VRES       | Power	VRES			          |               | +3.3V         |
| 75        | CONFIG_2  |            | Defines Module Type	NC	           |              |               |

