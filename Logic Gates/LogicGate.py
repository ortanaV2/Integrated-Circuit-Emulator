def convertOutput(inp):
    if type(inp) == bool:
        if inp: return 1
        return 0
    if type(inp) == int:
        if inp == 1: return True
        return False
        
class LogicGate:
    def __init__(self) -> None:
        self.returnType = bool

    def returnInt(self): self.returnType = int
    def returnBool(self): self.returnType = bool

    def output(self, type_):
        if type_ and self.returnType == bool: return True
        if not type_ and self.returnType == bool: return False
        if type_ and self.returnType == int: return 1
        if not type_ and self.returnType == int: return 0

    class And:
        @staticmethod
        def inp2(a: bool, b: bool) -> bool: return a and b
        @staticmethod
        def inp4(a: bool, b: bool, c: bool, d: bool) -> bool: return a and b and c and d

    class Or:
        @staticmethod
        def inp2(a: bool, b: bool) -> bool: return a or b
        @staticmethod
        def inp4(a: bool, b: bool, c: bool, d: bool) -> bool: return a or b or c or d

    class Not:
        @staticmethod
        def inp(a: bool) -> bool: return not a

    class Nand:
        @staticmethod
        def inp2(a: bool, b: bool) -> bool: return not (a and b)
        @staticmethod 
        def inp4(a: bool, b: bool, c: bool, d: bool) -> bool: return not (a and b and c and d)

    class Nor:
        @staticmethod
        def inp2(a: bool, b: bool) -> bool: return not (a or b)
        @staticmethod
        def inp4(a: bool, b: bool, c: bool, d: bool) -> bool: return not (a or b or c or d)

    class Xor:
        @staticmethod
        def inp2(a: bool, b: bool) -> bool: return (a and not b) or (not a and b)

    class Xnor:
        @staticmethod
        def inp2(a: bool, b: bool) -> bool: return not ((a and not b) or (not a and b))

#Examples:
gate = LogicGate()
print(gate.output(LogicGate.Or.inp2(True, False)))
print(gate.output(LogicGate.Not.inp(False)))
print(gate.output(LogicGate.Nor.inp2(False, False)))
print(gate.output(LogicGate.Xnor.inp2(False, False)))

gate.returnInt()
print(gate.output(LogicGate.Or.inp2(True, False)))
print(gate.output(LogicGate.Not.inp(False)))
print(gate.output(LogicGate.Nor.inp2(False, False)))
print(gate.output(LogicGate.Xnor.inp2(False, False)))
