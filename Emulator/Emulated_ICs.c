#include <stdio.h>
#include <stdbool.h>
#include <string.h>

void Multiplexer_CD74HCT151E(bool C, bool B, bool A, bool DATA[], int data_length, bool ENABLE, bool output[2]) {
    int dataInputIndex = (A * 1) + (B * 2) + (C * 4);
    bool dataInputs[8] = {false};

    for (int i = 0; i < 8; i++) {
        if (i < data_length) {
            dataInputs[i] = DATA[i];
        } else {
            dataInputs[i] = false;
        }
    }

    if (!ENABLE) {
        output[0] = dataInputs[dataInputIndex];
        output[1] = !dataInputs[dataInputIndex]; // return [Y = normal, W = inverted]
    } else {
        output[0] = true;
        output[1] = false;
    }
}

void Demultiplexer_CD74HCT238E(bool G2, bool nG1, bool nG0, bool C, bool B, bool A, bool output[8]) {
    bool falseList[8] = {false};

    if (!G2 || nG0 || nG1) {
        memcpy(output, falseList, 8 * sizeof(bool));
        return;
    }

    int dataInputIndex = (A * 1) + (B * 2) + (C * 4);
    falseList[dataInputIndex] = true;
    memcpy(output, falseList, 8 * sizeof(bool));
}

// Shiftregister_SN74LS165AN
typedef struct {
    bool register_[8];
    bool clk;
} Shiftregister_SN74LS165AN;

void Shiftregister_SN74LS165AN_init(Shiftregister_SN74LS165AN *reg) {
    memset(reg->register_, false, 8 * sizeof(bool));
    reg->clk = false;
}

void Shiftregister_SN74LS165AN_Pins(Shiftregister_SN74LS165AN *reg, bool CLK, bool CLK_INH, bool SH_nLD, bool SER, bool REGISTER_INPUTS[], int reg_input_length, bool output[2]) {
    if (!SH_nLD) { // Load RegisterInputs into register
        for (int i = 0; i < 8; i++) {
            if (i < reg_input_length) {
                reg->register_[i] = REGISTER_INPUTS[i];
            } else {
                reg->register_[i] = false;
            }
        }
    } else {
        if ((CLK && !reg->clk) && CLK_INH) { // Rising Edge + CLK not inhibited
            memmove(&reg->register_[1], &reg->register_[0], 7 * sizeof(bool));
            reg->register_[0] = SER;
        }
    }

    reg->clk = CLK;
    output[0] = reg->register_[7]; // return [Qh = normal, nQh = inverted]
    output[1] = !reg->register_[7];
}

// Basic 2-INP Logic Gates
bool INVERT_CD40106BE(bool A) { return !A; }
bool AND_CD4081BE(bool A, bool B) { return A && B; }
bool NAND_CD4011BE(bool A, bool B) { return !(A && B); }
bool OR_CD4071BE(bool A, bool B) { return A || B; }
bool NOR_CD4001BE(bool A, bool B) { return !(A || B); }
bool XOR_CD4030BE(bool A, bool B) { return (A && !B) || (!A && B); }
bool XNOR_CD4077BE(bool A, bool B) { return !((A && !B) || (!A && B)); }

int main() {
    Shiftregister_SN74LS165AN regA;
    Shiftregister_SN74LS165AN_init(&regA);

    bool regA_Qh_output[2];
    bool regA_REGISTER_INPUTS[8] = {true, true, true, true, true, true, true, true};
    Shiftregister_SN74LS165AN_Pins(&regA, false, false, false, false, regA_REGISTER_INPUTS, 8, regA_Qh_output);

    bool OUTPUT[2];
    bool DATA[1] = {regA_Qh_output[0]};
    Multiplexer_CD74HCT151E(false, false, false, DATA, 1, false, OUTPUT);

    printf("%d\n", regA_Qh_output[0]); // Print regA_Qh
    printf("%d\n", OUTPUT[0]); // Print OUTPUT

    return 0;
}
