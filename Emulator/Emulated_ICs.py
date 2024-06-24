class ICs:
    def Multiplexer_CD74HCT151E(C: bool = False, B: bool = False, A: bool = False, DATA: list[bool] = [], ENABLE: bool = False) -> list[bool]: 
        dataInputIndex = sum([i[1] for i in [(A, 1), (B, 2), (C, 4)] if i[0]])
        dataInputs = []
        for i in range(7):
            if len(DATA) - 1 >= i: dataInputs.append(DATA[i])
            else: dataInputs.append(False)
        if not ENABLE: return [not (dataInputs[dataInputIndex]), dataInputs[dataInputIndex]] # return [Y = normal, W = inverted]
        return [True, False]
    
    def Demultiplexer_CD74HCT238E(G2: bool = False, nG1: bool = False, nG0: bool = False, C: bool = False, B: bool = False, A: bool= False) -> list[bool]:
        falseList = [False] * 8
        if (not G2) or nG0 or nG1: return falseList
        dataInputIndex = sum([i[1] for i in [(A, 1), (B, 2), (C, 4)] if i[0]])
        falseList[dataInputIndex] = True        
        return falseList
    
    class Shiftregister_SN74LS165AN:
        def __init__(self) -> None:
            self.register = [False] * 8
            self.clk = False
    
        def Pins(self, CLK: bool = False, CLK_INH: bool = False, SH_nLD: bool = False, SER: bool = False, REGISTER_INPUTS: list[bool] = [False] * 8) -> list[bool]:
            if not SH_nLD:  # Load RegisterInputs into register
                self.register = []
                for i in range(8):
                    if len(REGISTER_INPUTS) - 1 >= i:
                        self.register.append(REGISTER_INPUTS[i])
                    else:
                        self.register.append(False)
            else:
                if (CLK and not self.clk) and CLK_INH:  # Rising Edge + CLK not inhibited
                    self.register.insert(0, SER)
                    self.register.pop()
            
            self.clk = CLK
            
            return ([self.register[-1], not self.register[-1]], self.register) # return [Qh = normal, nQh = inverted]

    # Basic 2-INP Logic Gates: 
    def INVERT_CD40106BE(A: bool = False) -> bool: return not A
    def AND_CD4081BE(A: bool = False, B: bool = False) -> bool: return A and B
    def NAND_CD4011BE(A: bool = False, B: bool = False) -> bool: return not (A and B)
    def OR_CD4071BE(A: bool = False, B: bool = False) -> bool: return A or B
    def NOR_CD4001BE(A: bool = False, B: bool = False) -> bool: return not (A or B)
    def XOR_CD4030BE(A: bool = False, B: bool = False) -> bool: return (A and not B) or (not A and B)
    def XNOR_CD4077BE(A: bool = False, B: bool = False) -> bool: return not ((A and not B) or (not A and B))

print(ICs.Multiplexer_CD74HCT151E(C=False, B=False, A=False, DATA=[False, True, True, True, False, True, True, False]))
print(ICs.Demultiplexer_CD74HCT238E(G2=True, C=True, B=True, A=False))

# Shiftregister Code Example:
clock = False
SER_ = True
register1 = ICs.Shiftregister_SN74LS165AN()
for i in range(20):
    clock = not clock
    print(register1.Pins(CLK=clock, CLK_INH=True, SH_nLD=True, SER=SER_))
    SER_ = False
