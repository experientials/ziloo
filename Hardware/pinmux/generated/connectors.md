<!-- GENERATED from pins.yaml by render.py — do not hand-edit. -->

## Connector registry

First-class connectors beyond the P20/P21/P10 headers. `given` = vendor-fixed · `placed` = drawn in KiCad · `draft` = planned.

| Connector | Board | Type | Pos | Status | Part | Pinout | How it connects |
|---|---|---|---|---|---|---|---|
| **929 Faceboard M.2 Key B** | 929-faceboard | m2_socket Key B | 67 | placed | Amphenol 10128793-001RLF | [doc](../pinouts/M2_KEY_B_CONNECTOR.md) | SoM via P20/P21 — SAI5 I2S spk+mic (TXC/TXFS/TXD0/RXFS/RXD0), SD2 Key-M (DATA0-3/CMD/CLK), PCIe (RXN±/TXN±/REFCLK±/CLKREQ/WAKE/PERST), USB2 D±, USB3 SSTX/SSRX±, I2C3 (GNSS/STEM), UART2 (COEX/LoRa/debug) |
| **SB-UCM eval-carrier M.2 (P9)** | sb-ucm-imx8plus-carrier | m2_socket Key B | 67 | given | CompuLab carrier ref P9 (M.2 B-key) | — | SoM PCIe x1 (modem) + SATA/SDIO (SSD) + USB per CompuLab carrier design |
| **Product M.2 (planned)** | product | m2_socket Key B? | 67 | draft | — | [doc](../pinouts/M2_KEY_B_CONNECTOR.md) | current plan = Key B (WWAN/LoRa/SIM + storage); type not locked |

**Product M.2 (planned)** — DRAFT — keying B/E/M undecided; current plan follows the 929 Key B. Revisit before layout. _Alt:_ Key E (WiFi/BT WNFB-266XI over SD1/UART2) — ../pinouts/M2_KEY_E_CONNECTOR.md
