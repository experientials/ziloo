# How to manage the sub-systems

The SoM can be woken up by raising `PMIC_ON_REQ` and be put to sleep by raising `PMIC_STBY_REQ`.

Should `POR_B` from the SoM trigger reset of camera modules?


Access PMIC with I2C on user space
https://community.nxp.com/t5/i-MX-Processors/Access-PMIC-with-I2C-on-user-space/m-p/599273

PCA9450 and multiple time programmable registers
https://community.nxp.com/t5/i-MX-Processors/PCA9450-and-multiple-time-programmable-registers/m-p/1434758
