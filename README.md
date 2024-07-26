# TIICBC Controller (Serial Input & CLK) + Emulator Set
## TIICBC CPU Main Module
The main module contains crucial logic like the jump-instruction, program counter, line addressing etc..

![](https://github.com/ortanaV2/TIICBC-Controller-Emulator/blob/main/IMG_20240723_190550167~2.jpg?raw=true)
## Serial Input & CLK *[OUTDATED]*
Controlled by the ESP8266 microcontroller. The input data and the CLK is controlled by the microcontroller which has 3 output pins (CLK, TRANSFER_STATE, DATA_INPUT). Circuit picture:

![](https://github.com/ortanaV2/TIICBC_Controller/blob/main/IMG_20240619_224204790~2.jpg?raw=true)
## Emulator & Datasheets
The TIICBC emulator is able to emulate various systems that can be digitally traced and analyzed step by step. Any circuit can be created using the classes and methods that are the IC objects. These are the datasheets for the ICs:
![](https://github.com/ortanaV2/TIICBC-Controller-Emulator/blob/main/Emulator%20Datasheets/CD4011BE.png?raw=true)
![](https://github.com/ortanaV2/TIICBC-Controller-Emulator/blob/main/Emulator%20Datasheets/CD40106BE.png?raw=true)
![](https://github.com/ortanaV2/TIICBC-Controller-Emulator/blob/main/Emulator%20Datasheets/CD4011BE.png?raw=true)
![](https://github.com/ortanaV2/TIICBC-Controller-Emulator/blob/main/Emulator%20Datasheets/CD4030BE.png?raw=true)
![](https://github.com/ortanaV2/TIICBC-Controller-Emulator/blob/main/Emulator%20Datasheets/CD4071BE.png?raw=true)
![](https://github.com/ortanaV2/TIICBC-Controller-Emulator/blob/main/Emulator%20Datasheets/CD4077BE.png?raw=true)
![](https://github.com/ortanaV2/TIICBC-Controller-Emulator/blob/main/Emulator%20Datasheets/CD4081BE.png?raw=true)
![](https://github.com/ortanaV2/TIICBC-Controller-Emulator/blob/main/Emulator%20Datasheets/CD74HCT151E.png?raw=true)
![](https://github.com/ortanaV2/TIICBC-Controller-Emulator/blob/main/Emulator%20Datasheets/CD74HCT238E.png?raw=true)
![](https://github.com/ortanaV2/TIICBC-Controller-Emulator/blob/main/Emulator%20Datasheets/SN74LS165AN.png?raw=true)
