class SA:

    def __init__(self, TS):
        self.TS = TS
        self.index = 0
        if (self.S()):
            if (self.TS[self.index].CP in {'$'}):
                print("Syntax is correct")
            else:
                print("Syntax error in line ", self.TS[self.index].line_no)
        else:
            print("Syntax error in line ", self.TS[self.index].line_no)
        
    
    def S(self):
        print("Entering S")
        if self.TS[self.index].CP in {'import', 'from', 'void'}:
            if self.import_st():
                if self.TS[self.index].CP == 'void':
                    self.index += 1
                    if self.TS[self.index].CP == 'ID':
                        self.index += 1
                        if self.TS[self.index].CP == '{':
                            self.index += 1
                            if self.TS[self.index].CP == '}':
                                self.index += 1
                                if self.TS[self.index].CP == ':':
                                    self.index += 1
                                    if self.body1():
                                        if self.defs():
                                            print("Exiting S: True")
                                            return True
            
        print("Exiting S: False")
        return False

    def import_st(self):
        print("Entering import_st")
        if (self.TS[self.index].CP in {'import', 'from', 'void'}):
            if self.TS[self.index].CP == 'import':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == 'from':
                        self.index += 1
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.TS[self.index].CP == 'ln':
                                self.index += 1
                                print("Exiting import_st: True")
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else: 
                    return False
                
            elif self.TS[self.index].CP == 'from':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == 'import':
                        self.index += 1
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.TS[self.index].CP == 'ln':
                                self.index += 1
                                print("Exiting import_st: True")
                                return True
                            else:
                                return False
                        else:
                            return False
                    else: 
                        return False
                else:
                    return False
            return True
        print("Exiting import_st: False")
        return False

    def AE_prime(self):
        print(f"Entering AE_prime at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'LO2', ')', ']', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', '}', ','}:
            if self.TS[self.index].CP == 'LO2':
                self.index += 1
                if self.RE2():
                    if self.AE_prime():
                        print("Exiting AE_prime: True")
                        return True
                    else:
                        return False
                else: 
                    return False
            print("Exiting AE_prime: True (default path)")
            return True
        print("Exiting AE_prime: False")
        return False

    def AE(self):
        print(f"Entering AE at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', 'TS', 'ID', '{'}:
            if self.RE2():
                if self.AE_prime():
                    print("Exiting AE: True")
                    return True
            # If any condition fails, return False
        print("Exiting AE: False")
        return False

    def E_prime(self):
        print(f"Entering E_prime at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'PM', ')', ']', ',', '}', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2', 'RO1', 'RO2'}:
            if self.TS[self.index].CP == 'PM':
                self.index += 1
                if self.T():
                    if self.E_prime():
                        print("Exiting E_prime: True")
                        return True
                    else:
                        return False
                else: 
                    return False
                    
            return True
        return False

    def E(self):
        print(f"Entering E at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', 'TS', 'ID', '{'}:
            if self.T():
                if self.E_prime():
                    print("Exiting E: True")
                    return True
            # If any condition fails, return False
        return False

    def F1(self):
        print(f"Entering F1 at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {')', ']', '}', ',', '{', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2', 'RO1', 'RO2', 'PM', 'MDME', 'instanceof'}:
            if self.TS[self.index].CP == '{':
                self.index += 1
                if self.args_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        print("Exiting F1: True ({ path)")
                        return True
                    else:
                        return False
                else: 
                    return False
                
            elif self.TS[self.index].CP == 'instanceof':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    print("Exiting F1: True (instanceof path)")
                    return True
                else:
                    return False
            print("Exiting F1: True (default path)")
            return True
        return False

    def F(self):
        print(f"Entering F at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', 'TS', 'ID', '{'}:
            if self.const():
                print("Exiting F: True (const path)")
                return True
            elif self.TS[self.index].CP == '{':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        print("Exiting F: True (OE path)")
                        return True
            elif self.TS[self.index].CP == 'LO1':
                self.index += 1
                if self.F():
                    print("Exiting F: True (LO1 path)")
                    return True
            elif self.TS[self.index].CP == 'TS':
                self.index += 1
                if self.TS[self.index].CP == '.':
                    self.index += 1
                    if self.TS[self.index].CP == 'ID':
                        self.index += 1
                        if self.option():
                            if self.F1():
                                print("Exiting F: True (TS path)")
                                return True
            elif self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.option():
                    if self.F1():
                        print("Exiting F: True (ID path)")
                        return True
        return False

    def MST(self):
        print(f"Entering MST at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'DT', 'String', 'dict', 'TS', 'ID', 'if', 'while', 'try', 'throw', 'FlowControl', 'return', ')'}:
            if self.SST():
                if self.MST():
                    print("Exiting MST: True (recursive path)")
                    return True
                else:
                    return False
                
            print("Exiting MST: True (default path)")
            return True
        return False

    def RE1_prime(self):
        print(f"Entering RE1_prime at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'RO2', ')', ']', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2', 'RO1', '}', ','}:
            if self.TS[self.index].CP == 'RO2':
                self.index += 1
                if self.E():
                    if self.RE1_prime():
                        print("Exiting RE1_prime: True (RO2 path)")
                        return True
                    else:
                        return False
                else:
                    return False
            print("Exiting RE1_prime: True (default path)")
            return True
        return False

    def RE1(self):
        print(f"Entering RE1 at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', 'TS', 'ID', '{'}:
            if self.E():
                if self.RE1_prime():
                    print("Exiting RE1: True")
                    return True
            # If any condition fails, return False
        return False

    def OE_prime(self):
        print(f"Entering OE_prime at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'LO2', ')', ']', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', '}', ','}:
            if self.TS[self.index].CP == 'LO2':
                self.index += 1
                if self.AE():
                    if self.OE_prime():
                        print("Exiting OE_prime: True (LO2 path)")
                        return True
                    else:
                        return False
                else:
                    return False
            print("Exiting OE_prime: True (default path)")
            return True
        return False

    def OE(self):
        if self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', 'TS', 'ID', "{"}:
            if self.AE():
                if self.OE_prime():
                    return True
            # If any condition fails, return False
        return False

    def RE2_prime(self):
        if self.TS[self.index].CP in {'RO1', ')', ']', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2', '}', ','}:
            if self.TS[self.index].CP == 'RO1':
                self.index += 1
                if self.RE1():
                    if self.RE2_prime():
                        return True
                    else:
                        return False
                else:
                    return False
            return True
        return False

    def RE2(self):
        if self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', 'TS', 'ID', '{'}:
            if self.RE1():
                if self.RE2_prime():
                    return True
            # If any condition fails, return False
        return False

    def SST_prime(self):
        if self.TS[self.index].CP in {'DT', 'String', 'dict', 'TS', 'ID', 'if', 'while', 'try', 'throw', 'flowControl', 'return', ')', '.', '[', '(', '=', 'COMPASS', 'instanceof', 'ID'}:
            if self.option():
                if self.SST2():
                    return True
            elif self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.dec2():
                    if self.TS[self.index].CP == 'ln':
                        self.index += 1
                        return True
            # If any condition fails, return False
        return False

    def SST2(self):
        if self.TS[self.index].CP in {'ln', '=', 'COMPASS', 'instanceof'}:
            if self.TS[self.index].CP == 'ln':
                self.index += 1
                return True
            elif self.TS[self.index].CP == '=':
                self.index += 1
                if self.SST3():
                    return True
            elif self.TS[self.index].CP == 'COMPASS':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == 'ln':
                        self.index += 1
                        return True
            elif self.TS[self.index].CP == 'instanceof':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == 'ln':
                        self.index += 1
                        return True
            # If any condition fails, return False
        return False

    def SST3(self):
        if self.TS[self.index].CP in {'new', 'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', 'TS', 'ID', '{'}:
            if self.OE():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    return True
            elif self.TS[self.index].CP == 'new':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == '{':
                        self.index += 1
                        if self.args_list():
                            if self.TS[self.index].CP == '}':
                                self.index += 1
                                if self.TS[self.index].CP == 'ln':
                                    self.index += 1
                                    return True
            # If any condition fails, return False
        return False

    def SST(self):
        if self.TS[self.index].CP in {'DT', 'String', 'dict', 'TS', 'ID', 'if', 'while', 'flowControl', 'try', 'throw'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec1():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            return True
            elif self.TS[self.index].CP == 'String':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec1():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            return True
            elif self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec3():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            return True
            elif self.TS[self.index].CP == 'TS':
                self.index += 1
                if self.TS[self.index].CP == '.':
                    self.index += 1
                    if self.TS[self.index].CP == 'ID':
                        self.index += 1
                        if self.option():
                            if self.SST2():
                                return True
            elif self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.SST_prime():
                    return True
            elif self.ifelse_st():
                return True
            elif self.while_st():
                return True
            elif self.TS[self.index].CP == 'flowControl':
                self.index += 1
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    return True
            elif self.trycatch_st():
                return True
            elif self.throw_st():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    return True
            # If any condition fails, return False
        return False

    def T_prime(self):
        print(f"Entering T_prime at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'MDME', ')', ']', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2', 'RO1', 'RO2', 'PM', '}', ','}:
            if self.TS[self.index].CP == 'MDME':
                self.index += 1
                if self.F():
                    if self.T_prime():
                        print("Exiting T_prime: True (MDME path)")
                        return True
                    else:
                        return False
                else:
                    return False
            return True
        return False

    def T(self):
        print(f"Entering T at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', 'TS', 'ID', '{'}:
            if self.F():
                if self.T_prime():
                    print("Exiting T: True")
                    return True
            # If any condition fails, return False
        print("Exiting T: False")
        return False

    def amh3(self):
        if self.TS[self.index].CP in {'final', 'DT', 'String', 'dict', 'ID', 'void'}:
            if self.TS[self.index].CP == 'final':
                self.index += 1
                return True
            return True
        return False

    def args_list(self):
        if self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', 'TS', 'ID', '{', '}'}:
            if self.OE():
                if self.list_args():
                    return True
                else:
                    return False
                
            return True
        return False

    def list_args(self):
        if self.TS[self.index].CP in {',', '}'}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.OE():
                    if self.list_args():
                        return True
                    else:
                        return False
                else:
                    return False
                
            return True
        return False

    def arr_mul(self):
        if self.TS[self.index].CP in {'[', 'ID'}:
            if self.TS[self.index].CP == '[':
                self.index += 1
                if self.TS[self.index].CP == ']':
                    self.index += 1
                    if self.arr_mul():
                        return True
                    else:
                        return False
                else:
                    return False
                
            return True
        return False

    def arr_size(self):
        if self.TS[self.index].CP in {'[', '=', 'AM', 'static', 'final', 'String', 'DT', 'ID', 'dict', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return', ','}:
            if self.TS[self.index].CP == '[':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == ']':
                        self.index += 1
                        if self.arr_size():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            return True
        return False

    def arr_val_values_prime(self):
        if self.TS[self.index].CP in {',', ']'}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.values():
                    return True
                else:
                    return False
                
            return True
        return False

    def body1(self):
        if self.TS[self.index].CP in {'('}:
            if self.TS[self.index].CP == '(':
                self.index += 1
                if self.MST():
                    if self.return_st():
                        if self.TS[self.index].CP == ')':
                            self.index += 1
                            return True
            # If any condition fails, return False
        return False

    def body(self):
        if self.TS[self.index].CP in {'(', 'ln'}:
            if self.TS[self.index].CP == '(':
                self.index += 1
                if self.MST():
                    if self.return_st():
                        if self.TS[self.index].CP == ')':
                            self.index += 1
                            return True
            elif self.TS[self.index].CP == 'ln':
                self.index += 1
                return True
            # If any condition fails, return False
        return False

    def const(self):
        print(f"Entering const at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const'}:
            self.index += 1
            return True
        return False

    def extends_st(self):
        if self.TS[self.index].CP in {'extends', 'implements', ':'}:
            if self.TS[self.index].CP == 'extends':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    return True
                else:
                    return False
                
            return True
        return False

    def implements_st(self):
        if self.TS[self.index].CP in {'implements', ':'}:
            if self.TS[self.index].CP == 'implements':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.interface_rec():
                        return True
                    else:
                        return False
                else:
                    return False
            return True
        return False

    def interface_rec(self):
        if self.TS[self.index].CP in {',', ':'}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.interface_rec():
                        return True
                    else:
                        return False
                else:
                    return False
            return True
        return False

    def defs(self):
        if self.TS[self.index].CP in {'DT', 'String', 'void', 'ID', 'dict', 'class', 'AM', 'final', 'interface', 'enum', '$', 'ln'}:
            if self.func_def():
                if self.defs():
                    return True
                else:
                    return False
            elif self.TS[self.index].CP == 'class':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.extends_st():
                        if self.implements_st():
                            if self.TS[self.index].CP == ':':
                                self.index += 1
                                if self.TS[self.index].CP == '(':
                                    self.index += 1
                                    if self.class_body():
                                        if self.TS[self.index].CP == ')':
                                            self.index += 1
                                            if self.defs():
                                                return True
                                            else:
                                                return False
                                        else:
                                            return False
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else: 
                    return False
                
            elif self.TS[self.index].CP == 'AM':
                self.index += 1
                if self.defs2():
                    return True
                else:
                    return False
                
            elif self.TS[self.index].CP == 'final':
                self.index += 1
                if self.TS[self.index].CP == 'class':
                    self.index += 1
                    if self.TS[self.index].CP == 'ID':
                        self.index += 1
                        if self.extends_st():
                            if self.implements_st():
                                if self.TS[self.index].CP == ':':
                                    self.index += 1
                                    if self.TS[self.index].CP == '(':
                                        self.index += 1
                                        if self.class_body():
                                            if self.TS[self.index].CP == ')':
                                                self.index += 1
                                                if self.defs():
                                                    return True
                                                else:
                                                    return False
                                            else:
                                                return False
                                        else:
                                            return False
                                    else:
                                        return False  
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False  
            elif self.TS[self.index].CP == 'interface':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.extends_st_interface():
                        print("exint se andr agya")
                        if self.TS[self.index].CP == ':':
                            self.index += 1
                            if self.TS[self.index].CP == '(':
                                self.index += 1
                                if self.interface_body():
                                    if self.TS[self.index].CP == ')':
                                        self.index += 1
                                        if self.defs():
                                            return True
                                        else:
                                            return False
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif self.enum_def():
                if self.defs():
                    return True
                else:
                    return False
            return True
            # If any condition fails, return False
        return False

    def defs2(self):
        if self.TS[self.index].CP in {'final', 'class', 'interface'}:
            if self.ch2():
                if self.TS[self.index].CP == 'class':
                    self.index += 1
                    if self.TS[self.index].CP == 'ID':
                        self.index += 1
                        if self.extends_st():
                            if self.implements_st():
                                if self.TS[self.index].CP == ':':
                                    self.index += 1
                                    if self.TS[self.index].CP == '(':
                                        self.index += 1
                                        if self.class_body():
                                            if self.TS[self.index].CP == ')':
                                                self.index += 1
                                                if self.defs():
                                                    return True
                                                else:
                                                    return False
                                            else:
                                                return False
                                        else:
                                            return False
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif self.TS[self.index].CP == 'interface':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.extends_st_interface():
                        if self.TS[self.index].CP == ':':
                            self.index += 1
                            if self.TS[self.index].CP == '(':
                                self.index += 1
                                if self.interface_body():
                                    if self.TS[self.index].CP == ')':
                                        self.index += 1
                                        if self.defs():
                                            return True
                                        else:
                                            return False
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else: 
                return False
                # If any condition fails, return False
        return False
    
    def ch2(self):
        if self.TS[self.index].CP in {'final', 'class'}:
            if self.TS[self.index].CP == 'final':
                self.index += 1
                return True
            return True
            # If any condition fails, return False
        return False
    
    def extends_st_interface(self):
        if self.TS[self.index].CP in {'extends', ':'}:
            if self.TS[self.index].CP == 'extends':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.interface_rec():
                        return True
                    else:
                        return False
                else:
                    return False
                # If any condition fails, return False
            return True
        return False

    def interface_body(self):
        if self.TS[self.index].CP in {'AM', 'DT', 'String', 'ID', 'dict'}:
            if self.TS[self.index].CP == 'AM':
                self.index += 1
                if self.ifb2():
                    return True
            elif self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.ifb3():
                    return True
            elif self.TS[self.index].CP == 'String':
                self.index += 1
                if self.ifb3():
                    return True
            elif self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.ifb4():
                    return True
            elif self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.ifb5():
                    return True
                # If any condition fails, return False
        return False

    def ifb2(self):
        if self.TS[self.index].CP in {'static', 'DT', 'String', 'ID', 'dict'}:
            if self.TS[self.index].CP == 'static':
                self.index += 1
                if self.TS[self.index].CP == 'final':
                    self.index += 1
                    if self.dec():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.interface_body():
                                return True
            elif self.func_def_interface():
                if self.interface_body():
                    return True
            # If any condition fails, return False
        return False

    def ifb3(self):
        if self.TS[self.index].CP in {'ID', '['}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.ifb3a():
                    return True
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.TS[self.index].CP == ']':
                    self.index += 1
                    if self.arr_mul():
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.TS[self.index] == '{':
                                self.index += 1
                                if self.params_list():
                                    if self.TS[self.index].CP == '}':
                                        self.index += 1
                                        if self.TS[self.index].CP == 'ln':
                                            self.index += 1
                                            return True
            # If any condition fails, return False
        return False

    def ifb4(self):
        if self.TS[self.index].CP in {'ID', '['}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.ifb4a():
                    return True
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.TS[self.index].CP == ']':
                    self.index += 1
                    if self.arr_mul():
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.TS[self.index].CP == '{':
                                self.index += 1
                                if self.params_list():
                                    if self.TS[self.index].CP == '}':
                                        self.index += 1
                                        if self.TS[self.index].CP == 'ln':
                                            self.index += 1
                                            return True
            # If any condition fails, return False
        return False

    def ifb5(self):
        if self.TS[self.index].CP in {'ID', '['}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.ifb5a():
                    return True
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.TS[self.index].CP == ']':
                    self.index += 1
                    if self.arr_mul():
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.TS[self.index].CP == '{':
                                self.index += 1
                                if self.params_list():
                                    if self.TS[self.index].CP == '}':
                                        self.index += 1
                                        if self.TS[self.index].CP == 'ln':
                                            self.index += 1
                                            return True
            # If any condition fails, return False
        return False

    def cb2(self):
        if self.TS[self.index].CP in {'DT', 'String', 'ID', 'dict', 'void'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.cb2a():
                    return True
            elif self.TS[self.index].CP == 'String':
                self.index += 1
                if self.cb2a():
                    return True
            elif self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.cb2c():
                    return True
            elif self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.cb2b():
                    return True
            elif self.TS[self.index].CP == 'void':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == '{':
                        self.index += 1
                        if self.params_list():
                            if self.TS[self.index].CP == '}':
                                self.index += 1
                                if self.TS[self.index].CP == ':':
                                    self.index += 1
                                    if self.body():
                                        if self.class_body():
                                            return True
            # If any condition fails, return False
        return False

    def fnd2(self):
        if self.TS[self.index].CP in {'ID', '['}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.TS[self.index].CP == '{':
                    self.index += 1
                    if self.params_list():
                        if self.TS[self.index].CP == '}':
                            self.index += 1
                            if self.TS[self.index].CP == ':':
                                self.index += 1
                                if self.body():
                                    return True
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.TS[self.index].CP == ']':
                    self.index += 1
                    if self.arr_mul():
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.TS[self.index].CP == '{':
                                self.index += 1
                                if self.params_list():
                                    if self.TS[self.index].CP == '}':
                                        self.index += 1
                                        if self.TS[self.index].CP == ':':
                                            self.index += 1
                                            if self.body():
                                                return True
            # If any condition fails, return False
        return False

    def init_var(self):
        if self.TS[self.index].CP in {'=', ',' , 'AM' , 'String' , 'DT' , 'ID' , 'dict' , 'static' , 'final' , 'void' ,  ')' , 'TS' , 'if' , 'while' , 'try' , 'throw' , 'FlowControl' , 'return'}:
            if self.TS[self.index].CP == '=':
                self.index += 1
                if self.OE():
                    return True
                else:
                    return False
            return True
        return False

    def list_var(self):
        if self.TS[self.index].CP in {',', 'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'FlowControl', 'return'}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.init_var():
                    if self.list_var():
                        return True
                    else:
                        return False
                else:
                    return False
            return True
        return False
    
    def init_arr(self):
        if self.TS[self.index].CP in {'=', ',', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', '}', 'TS', 'if', 'while', 'try', 'throw', 'FlowControl', 'return'}:
            if self.TS[self.index].CP == '=':
                self.index += 1
                if self.init_arr_b():
                    return True
                else:
                    return False
            return True
            # If any condition fails, return False
        return False

    def list_arr(self):
        if self.TS[self.index].CP in {',', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'FlowControl', 'return'}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == '[':
                        self.index += 1
                        if self.OE():
                            if self.TS[self.index].CP == ']':
                                self.index += 1
                                if self.init_arr():
                                    if self.list_arr():
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            return True
        return False

    def init(self):
        if self.TS[self.index].CP in {'=', ',', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'FlowControl', 'return'}:
            if self.TS[self.index].CP == '=':
                self.index += 1
                if self.init2():
                    return True
                else:
                    return False
            return True
            # If any condition fails, return False
        return False

    def list(self):
        if self.TS[self.index].CP in {'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'FlowControl', 'return'}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.list2():
                        return True
                    else:
                        return False
                else:
                    return False
                
            return True
        return False

    def init_dict(self):
        if self.TS[self.index].CP in {'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'FlowControl', 'return', '=', ','}:
            if self.TS[self.index].CP == '=':
                self.index += 1
                if self.init_dict_b():
                    return True
                else:
                    return False
            return True
            # If any condition fails, return False
        return False

    def list_dict(self):
        if self.TS[self.index].CP in {',', '}'}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.init_dict():
                    if self.list_dict():
                        return True
            elif self.TS[self.index].CP == '}':
                return True
        return False

    def params_list(self):
        if self.TS[self.index].CP in {'DT', 'String', 'dict', 'ID'}:
            if self.params():
                return True
            return True
        return False

    def params_list_prime(self):
        if self.TS[self.index].CP in {',', ')'}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.params_list():
                    return True
            elif self.TS[self.index].CP == ')':
                return True
        return False

    def enum_def(self):
        if self.TS[self.index].CP in {'enum'}:
            if self.TS[self.index].CP == 'enum':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == ':':
                        self.index += 1
                        if self.TS[self.index].CP == '(':
                            self.index += 1
                            if self.TS[self.index].CP == 'ID':
                                self.index += 1
                                if self.init_enum_def():
                                    if self.enum_list():
                                        if self.TS[self.index].CP == ')':
                                            self.index += 1
                                            return True
                # If any condition fails, return False
        return False
    
    def init_enum_def(self):
        if self.TS[self.index].CP in {'=', ',', ')'}:
            if self.TS[self.index].CP == '=':
                self.index += 1
                if self.OE():
                    return True
                else:
                    return False
            return True
        return False

    def enum_list(self):
        if self.TS[self.index].CP in {'}', ','}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.init_enum_def():
                        if self.enum_list():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            return True
        return False
    

    def class_body(self):
        if self.TS[self.index].CP in {'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', ')'}:
            if self.TS[self.index].CP == 'AM':
                self.index += 1
                if self.cb3():
                    return True
            elif self.TS[self.index].CP == 'static':
                self.index += 1
                if self.amh3():
                    if self.cb2():
                        return True
            elif self.TS[self.index].CP == 'final':
                self.index += 1
                if self.cb2():
                    return True
            elif self.cb2():
                return True
            elif self.TS[self.index].CP == ')':
                return True
                # If any condition fails, return False
        return False

    def cb3(self):
        if self.TS[self.index].CP in {'static', 'final', 'DT', 'String', 'dict', 'ID', 'void'}:
            if self.TS[self.index].CP == 'static':
                self.index += 1
                if self.amh3():
                    if self.cb2():
                        return True
                    
            elif self.TS[self.index].CP == 'final':
                self.index += 1
                if self.cb2():
                    return True
            elif self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.cb2a():
                    return True
            elif self.TS[self.index].CP == 'String':
                self.index += 1
                if self.cb2a():
                    return True
            elif self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.cb3a():
                    return True
            elif self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.cb2b():
                    return True
            elif self.TS[self.index].CP == 'void':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == '{':
                        self.index += 1
                        if self.params_list():
                            if self.TS[self.index].CP == '}':
                                self.index += 1
                                if self.TS[self.index].CP == ':':
                                    self.index += 1
                                    if self.body():
                                        if self.class_body():
                                            return True
            # If any condition fails, return False
        return False
            
    def func_def(self):
        if self.TS[self.index].CP in {'DT', 'String', 'void', 'ID', 'dict'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.fnd2():
                    return True
            elif self.TS[self.index].CP == 'String':
                self.index += 1
                if self.fnd2():
                    return True
            elif self.TS[self.index].CP == 'void':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == '{':
                        self.index += 1
                        if self.params_list():
                            if self.TS[self.index].CP == '}':
                                self.index += 1
                                if self.TS[self.index].CP == ':':
                                    self.index += 1
                                    if self.body():
                                        return True
            elif self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.fnd2():
                    return True
            elif self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.fnd2():
                    return True
                # If any condition fails, return False
        return False

    def dec(self):
        if self.TS[self.index].CP in {'DT', 'String', 'ID', 'dict'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec1():
                        return True
            elif self.TS[self.index].CP == 'String':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec1():
                        return True
            elif self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec2():
                        return True
            elif self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec3():
                        return True
                # If any condition fails, return False
        return False

    def while_st(self):
        if self.TS[self.index].CP in {'while'}:
            if self.TS[self.index].CP == 'while':
                self.index += 1
                if self.TS[self.index].CP == '{':
                    self.index += 1
                    if self.OE():
                        if self.TS[self.index].CP == '}':
                            self.index += 1
                            if self.TS[self.index].CP == ':':
                                self.index += 1
                                if self.body():
                                    return True
                # If any condition fails, return False
        return False

    def trycatch_st(self):
        if self.TS[self.index].CP in {'try'}:
            if self.TS[self.index].CP == 'try':
                self.index += 1
                if self.TS[self.index].CP == ':':
                    self.index += 1
                    if self.body1():
                        if self.TS[self.index].CP == 'catch':
                            self.index += 1
                            if self.TS[self.index].CP == '{':
                                self.index += 1
                                if self.TS[self.index].CP == 'ID':
                                    self.index += 1
                                    if self.TS[self.index].CP == 'ID':
                                        self.index += 1
                                    if self.TS[self.index].CP == '}':
                                        self.index += 1
                                        if self.TS[self.index].CP == ':':
                                            self.index += 1
                                            if self.body1():
                                                if self.TS[self.index].CP == 'finally':
                                                    self.index += 1
                                                    if self.TS[self.index].CP == ':':
                                                        self.index += 1
                                                        if self.body1():
                                                            return True
                # If any condition fails, return False
        return False

    def throw_st(self):
        if self.TS[self.index].CP in {'throw'}:
            if self.TS[self.index].CP == 'throw':
                self.index += 1
                if self.TS[self.index].CP == 'new':
                    self.index += 1
                    if self.TS[self.index].CP == 'ID':
                        self.index += 1
                        if self.TS[self.index].CP == '{':
                            self.index += 1
                            if self.args_list():
                                if self.TS[self.index].CP == '}':
                                    self.index += 1
                                    return True
                # If any condition fails, return False
        return False

    def return_st(self):
        if self.TS[self.index].CP in {'return', ')'}:
            if self.TS[self.index].CP == 'return':
                self.index += 1
                if self.OE():
                    return True
                else:
                    return False
                # If any condition fails, return False
            return True
        return False

    def values(self):
        if self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', 'TS', 'ID', '[', '{'}:
            if self.OE():
                if self.arr_val_values_prime():
                    return True
            elif self.value_list():
                if self.arr_val_values_prime():
                    return True
                # If any condition fails, return False
        return False
    
    def func_def_interface(self):
        if self.TS[self.index].CP in {'DT', 'String', 'ID', 'dict'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.fn_def_inter2():
                    return True
            elif self.TS[self.index].CP == 'String':
                self.index += 1
                if self.fn_def_inter2():
                    return True
            elif self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.fn_def_inter2():
                    return True
            elif self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.fn_def_inter2():
                    return True
            # If any condition fails, return False
        return False

 # Additional missing functions

    def cb2a(self):
        if self.TS[self.index].CP in {'ID', '['}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.cb2a1():
                    return True
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.TS[self.index].CP == ']':
                    self.index += 1
                    if self.arr_mul():
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.TS[self.index].CP == '{':
                                self.index += 1
                                if self.params_list():
                                    if self.TS[self.index].CP == '}':
                                        self.index += 1
                                        if self.TS[self.index].CP == ':':
                                            self.index += 1
                                            if self.body():
                                                if self.class_body():
                                                    return True
                # If any condition fails, return False
        return False

    def cb2b(self):
        if self.TS[self.index].CP in {'ID', '['}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.cb2b1():
                    return True
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.TS[self.index].CP == ']':
                    self.index += 1
                    if self.arr_mul():
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.TS[self.index].CP == '{':
                                self.index += 1
                                if self.params_list():
                                    if self.TS[self.index].CP == '}':
                                        self.index += 1
                                        if self.TS[self.index].CP == ':':
                                            self.index += 1
                                            if self.body():
                                                if self.class_body():
                                                    return True
                # If any condition fails, return False
        return False

    def cb3a(self):
        if self.TS[self.index].CP in {'ID', '[', '{'}:
            if self.cb2c():
                return True
            elif self.TS[self.index].CP == '{':
                self.index += 1
                if self.params_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.TS[self.index].CP == ':':
                            self.index += 1
                            if self.TS[self.index].CP == '(':
                                self.index += 1
                                if self.constr_body():
                                    if self.TS[self.index].CP == ')':
                                        self.index += 1
                                        if self.class_body():
                                            return True
                # If any condition fails, return False
        return False

    def cb2c(self):
        if self.TS[self.index].CP in {'ID', '['}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.cb2c1():
                    return True
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.TS[self.index].CP == ']':
                    self.index += 1
                    if self.arr_mul():
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.TS[self.index].CP == '{':
                                self.index += 1
                                if self.params_list():
                                    if self.TS[self.index].CP == '}':
                                        self.index += 1
                                        if self.TS[self.index].CP == ':':
                                            self.index += 1
                                            if self.body():
                                                if self.class_body():
                                                    return True
                # If any condition fails, return False
        return False

    def ifelse_st(self):
        if self.TS[self.index].CP in {'if'}:
            if self.TS[self.index].CP == 'if':
                self.index += 1
                if self.TS[self.index].CP == '{':
                    self.index += 1
                    if self.OE():
                        if self.TS[self.index].CP == '}':
                            self.index += 1
                            if self.TS[self.index].CP == ':':
                                self.index += 1
                                if self.body():
                                    if self.else_if():
                                        if self.else_st():
                                            return True
                # If any condition fails, return False
        return False
        
    def else_if(self):
        if self.TS[self.index].CP in {'elif', 'DT', 'String', 'dict', 'TS', 'ID', 'if', 'while', 'try', 'throw', 'FlowControl', 'return', ')', 'else'}:
            if self.TS[self.index].CP == 'elif':
                self.index += 1
                if self.TS[self.index].CP == '{':
                    self.index += 1
                    if self.OE():
                        if self.TS[self.index].CP == '}':
                            self.index += 1
                            if self.TS[self.index].CP == ':':
                                self.index += 1
                                if self.body():
                                    if self.else_if():
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
                # If any condition fails, return False
            return True
        return False
    
    def else_st(self):
        if self.TS[self.index].CP in {'else', 'DT', 'String', 'dict', 'TS', 'ID', 'if', 'while', 'try', 'throw', 'FlowControl', 'return', ')'}:
            if self.TS[self.index].CP == 'else':
                self.index += 1
                if self.body():
                    return True
                else:
                    return False
                # If any condition fails, return False
            return True
        return False
    
    def params(self):
        if self.TS[self.index].CP in {'DT', 'ID', 'String', 'dict'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.params2():
                    return True
            elif self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.params2():
                    return True
            elif self.TS[self.index].CP == 'String':
                self.index += 1
                if self.params2():
                    return True
            elif self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.params2():
                    return True
                # If any condition fails, return False
        return False
    
    def params2(self):
        if self.TS[self.index].CP in {'ID', '['}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.list_param():
                    return True
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.TS[self.index].CP == ']':
                    self.index += 1
                    if self.arr_mul():
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.list():
                                return True
                # If any condition fails, return False
        return False
    
    def list_param(self):
        if self.TS[self.index].CP in {',', '}'}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.params():
                    return True
                else:
                    return False
            return True
        return False

    
    def cb2a1(self):
        if self.TS[self.index].CP in {'=', '[', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', '{', ','}:
            if self.dec1():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.class_body():
                        return True
            elif self.TS[self.index].CP == '{':
                self.index += 1
                if self.params_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.TS[self.index].CP == ':':
                            self.index += 1
                            if self.body():
                                if self.class_body():
                                    return True
                # If any condition fails, return False
        return False
    
    def cb2b1(self):
        if self.TS[self.index].CP in {'=', '[', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', '{', ','}:
            if self.dec3():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.class_body():
                        return True
            elif self.TS[self.index].CP == '{':
                self.index += 1
                if self.params_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.TS[self.index].CP == ':':
                            self.index += 1
                            if self.body():
                                if self.class_body():
                                    return True
                # If any condition fails, return False
        return False
    
    def cb2c1(self):
        if self.TS[self.index].CP in {'=', '[', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', '{', ','}:
            if self.dec2():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.class_body():
                        return True
            elif self.TS[self.index].CP == '{':
                self.index += 1
                if self.params_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.TS[self.index].CP == ':':
                            self.index += 1
                            if self.body():
                                if self.class_body():
                                    return True
                # If any condition fails, return False
        return False

    
    def init_arr_b(self):
        if self.TS[self.index].CP in {'ID', '['}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.init_arr():
                    return True
            elif self.value_list():
                return True
                # If any condition fails, return False
        return False
    
    def value_list(self):
        if self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
                self.index += 1
                if self.values():
                    if self.TS[self.index].CP == ']':
                        self.index += 1
                        return True
                # If any condition fails, return False
        return False
    
    def init2(self):
        if self.TS[self.index].CP in {'new', 'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', 'TS', 'ID', '{'}:
            if self.TS[self.index].CP == 'new':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == '{':
                        self.index += 1
                        if self.args_list():
                            if self.TS[self.index].CP == '}':
                                self.index += 1
                                if self.list():
                                    return True
            elif self.OE():
                return True
                # If any condition fails, return False
        return False
    
    def list2(self):
        if self.TS[self.index].CP in {'=', ',', 'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'FlowControl', 'return'}:
            if self.init():
                if self.list():
                    return True
                # If any condition fails, return False
        return False
    
    def init_dict_b(self):
        if self.TS[self.index].CP in {'ID', '{'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.init_dict():
                    return True
                # If any condition fails, return False
            elif self.TS[self.index].CP == '{':
                self.index += 1
                if self.values_of_dic():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        return True
        return False
    
    def values_of_dic(self):
        if self.TS[self.index].CP in {'ID', '}'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.TS[self.index].CP == ':':
                    self.index += 1
                    if self.OE():
                        if self.dict_val():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
                # If any condition fails, return False
            return True
        return False
    
    def dict_val(self):
        if self.TS[self.index].CP in {',', '}'}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == ':':
                        self.index += 1
                        if self.OE():
                            if self.dict_val():
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
                # If any condition fails, return False
            return True
        return False
    
    def constr_body(self):
        if self.TS[self.index].CP in {'TS', 'DT', 'String', 'dict', 'ID', 'if', 'while', 'flowControl', 'try', 'throw', ')'}:
            if self.TS[self.index].CP == 'TS':
                self.index += 1
                if self.constr_body2():
                    return True
                else:
                    return False
            elif self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec1():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.MST():
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif self.TS[self.index].CP == 'String':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec1():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.MST():
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec3():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.MST():
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.SST_prime():
                    if self.MST():
                        return True
                    else:
                        return False
                else:
                    return False
            elif self.ifelse_st():
                if self.MST():
                    return True
                else:
                    return False
            elif self.while_st():
                if self.MST():
                    return True
                else:
                    return False
            elif self.TS[self.index].CP == 'flowControl':
                self.index += 1
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.MST():
                        return True
                    else:
                        return False
                else:
                    return False
            elif self.trycatch_st():
                if self.MST():
                    return True
                else:
                    return False
            elif self.throw_st():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.MST():
                        return True
                    else:
                        return False
                else:
                    return False
                # If any condition fails, return False
            return True
        return False
    
    def constr_body2(self):
        if self.TS[self.index].CP in {'.', '{'}:
            if self.TS[self.index].CP == '.':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.option():
                        if self.SST2():
                            if self.MST():
                                return True
            elif self.TS[self.index].CP == '{':
                self.index += 1
                if self.args_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.MST():
                                return True
                # If any condition fails, return False
        return False
    
    def ifb3a(self):
        if self.TS[self.index].CP in {'=', '['}:
            if self.dec1():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.interface_body():
                        return True
            elif self.TS[self.index].CP == '{':
                self.index += 1
                if self.params_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.interface_body():
                                return True
                # If any condition fails, return False
        return False
    
    def ifb4a(self):
        if self.TS[self.index].CP in {'=', '[', '{', ','}:
            if self.dec2():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.interface_body():
                        return True
            elif self.TS[self.index].CP == '{':
                self.index += 1
                if self.params_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.interface_body():
                                return True
                # If any condition fails, return False
        return False
    
    def ifb5a(self):
        if self.TS[self.index].CP in {'=', '[', ',', '{'}:
            if self.dec3():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.interface_body():
                        return True
            elif self.TS[self.index].CP == '{':
                self.index += 1
                if self.params_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.interface_body():
                                return True
                # If any condition fails, return False
        return False
    
    def fn_def_inter2(self):
        if self.TS[self.index].CP in {'ID', '['}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.TS[self.index].CP == '{':
                    self.index += 1
                    if self.params_list():
                        if self.TS[self.index].CP == '}':
                            self.index += 1
                            if self.TS[self.index].CP == 'ln':
                                self.index += 1
                                return True
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.TS[self.index].CP == ']':
                    self.index += 1
                    if self.arr_mul():
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.TS[self.index].CP == '{':
                                self.index += 1
                                if self.params_list():
                                    if self.TS[self.index].CP == '}':
                                        self.index += 1
                                        if self.TS[self.index].CP == 'ln':
                                            self.index += 1
                                            return True
                # If any condition fails, return False
        return False
    
    def option(self):
        print(f"Entering option at index {self.index}, token: {self.TS[self.index].CP}")
        if self.TS[self.index].CP in {'.', '[', '(', '{' '=', 'COMPASS', 'instanceof', 'ln', ')', ']', '}', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'LO3', 'LO2', 'RO1', 'RO2', 'PM', 'MDME', ','}:
            if self.TS[self.index].CP == '.':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.option():
                        print("Exiting option: True (. path)")
                        return True
                    else:
                        return False
                else:
                    return False
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == ']':
                        self.index += 1
                        if self.option():
                            print("Exiting option: True ([ path)")
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif self.TS[self.index].CP == '(':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == ')':
                        self.index += 1
                        if self.option():
                            print("Exiting option: True (( path)")
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif self.TS[self.index].CP == '{':
                self.index += 1
                if self.args_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.option2():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            return True
        return False

    def option2(self):
        if self.TS[self.index].CP in {'.', 'ln'}:
            if self.TS[self.index].CP == '.':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.option():
                        return True
            elif self.TS[self.index].CP == 'ln':
                self.index += 1
                return True
        return False
    
    def dec1(self):
        if self.TS[self.index].CP in {'=', ',', '[', 'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'FlowControl', 'return', 'ln'}:
            if self.init_var():
                if self.list_var():
                    print("list var")
                    return True
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == ']':
                        self.index += 1
                        if self.arr_size():
                            if self.init_arr():
                                if self.list_arr():
                                    return True
                # If any condition fails, return False
        return False
    
    def dec2(self):
        if self.TS[self.index].CP in {'=', ',', '[', 'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'FlowControl', 'return', 'ln'}:
            if self.init():
                if self.list():
                    return True
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == ']':
                        self.index += 1
                        if self.arr_size():
                            if self.init_arr():
                                if self.list_arr():
                                    return True
                # If any condition fails, return False
        return False
    
    def dec3(self):
        if self.TS[self.index].CP in {'=', ',', '[', 'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'FlowControl', 'return', 'ln'}:
            if self.init_dict():
                if self.list_dict():
                    return True
            elif self.TS[self.index].CP == '[':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == ']':
                        self.index += 1
                        if self.arr_size():
                            if self.init_arr():
                                if self.list_arr():
                                    return True
                # If any condition fails, return False
        return False
    
