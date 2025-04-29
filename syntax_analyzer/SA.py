
class SA:
    def __init__(self, token_stream):
        self.TS = token_stream
        self.index = 0
        
        if self.S():
            print(self.TS[self.index].CP)
            if self.TS[self.index].CP == "$":
                print("Syntax is correct")
                return
            else:
                print("Invalid  abcSyntax at line no : ", self.TS[self.index].line_no)
        else:
            print("Invalid Syntax at line no : ", self.TS[self.index].line_no)

    def OE(self):
        if self.AE():
            if self.OE_prime():
                return True

    def OE_prime(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'LO2'}:
            if self.TS[self.index].CP == 'LO2':
                self.index += 1
                if self.AE():
                    if self.OE_prime():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}', ')', ']', ',', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln'}:
            # Epsilon production
            return True
        return False

    def AE(self):
        if self.RE2():
            if self.AE_prime():
                return True

    def AE_prime(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'LO2'}:
            if self.TS[self.index].CP == 'LO2':
                self.index += 1
                if self.RE2():
                    if self.AE_prime():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}', ')', ']', ',', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3'}:
            # Epsilon production
            return True
        return False

    def RE2(self):
        if self.RE1():
            if self.RE2_prime():
                return True

    def RE2_prime(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'RO1'}:
            if self.TS[self.index].CP == 'RO1':
                self.index += 1
                if self.RE1():
                    if self.RE2_prime():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}', ')', ']', ',', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2'}:
            # Epsilon production
            return True
        return False

    def RE1(self):
        if self.E():
            if self.RE1_prime():
                return True

    def RE1_prime(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'RO2'}:
            if self.TS[self.index].CP == 'RO2':
                self.index += 1
                if self.E():
                    if self.RE1_prime():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}', ')', ']', ',', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2', 'RO1'}:
            # Epsilon production
            return True
        return False

    def E(self):
        if self.T():
            if self.E_prime():
                return True

    def E_prime(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'PM'}:
            if self.TS[self.index].CP == 'PM':
                self.index += 1
                if self.T():
                    if self.E_prime():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}', ')', ']', ',', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2', 'RO1', 'RO2'}:
            # Epsilon production
            return True
        return False

    def T(self):
        if self.F():
            if self.T_prime():
                return True

    def T_prime(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'MDME'}:
            if self.TS[self.index].CP == 'MDME':
                self.index += 1
                if self.F():
                    if self.T_prime():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}', ')', ']', ',', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2', 'RO1', 'RO2', 'PM'}:
            # Epsilon production
            return True
        return False

    def F(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const'}:
            if self.const():
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
            if self.TS[self.index].CP == '{':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'LO1'}:
            if self.TS[self.index].CP == 'L01':
                self.index += 1
                if self.F():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'TS'}:
            if self.TS[self.index].CP == 'TS':
                self.index += 1
                if self.TS[self.index].CP == '.':
                    self.index += 1
                    if self.TS[self.index].CP == 'ID':
                        self.index += 1
                        if self.option():
                            if self.F1():
                                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.option():
                    if self.F1():
                        return True
        return False
    
    def const(self):
        if self.TS[self.index].CP == 'str_const':
            self.index += 1
            return True
        elif self.TS[self.index].CP == 'num_const':
            self.index += 1
            return True
        elif self.TS[self.index].CP == 'char_const':
            self.index += 1
            return True
        elif self.TS[self.index].CP == 'bool_const':
            self.index += 1
            return True
        elif self.TS[self.index].CP == 'null_const':
            self.index += 1
            return True
        return False
    
    def F1(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'}', ')', ']', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2', 'RO1', 'RO2', 'PM', 'MDME'}:
            # Epsilon production
            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'instanceof'}:
            if self.TS[self.index].CP == 'instanceof':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
            if self.TS[self.index].CP == '{':
                self.index += 1
                if self.args_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        return True
        return False

    def S(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'import', 'from', 'void'}:
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
                                            return True
        return False

    def import_st(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'void'}:
            # Epsilon production
            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'import'}:
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
                                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'from'}:
            if self.TS[self.index].CP == 'from':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == 'import':
                        self.index += 1
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.TS[self.index].CP == 'ln':
                                self.index += 1
                                return True
        return False

    def body(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'('}:
            if self.TS[self.index].CP == '(':
                self.index += 1
                if self.MST():
                    if self.return_st():
                        if self.TS[self.index].CP == ')':
                            self.index += 1
                            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ln'}:
            if self.TS[self.index].CP == 'ln':
                self.index += 1
                return True
        return False

    def defs(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT', 'String', 'void', 'ID', 'dict'}:
            if self.func_def():
                if self.defs():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'class'}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'AM'}:
            if self.TS[self.index].CP == 'AM':
                self.index += 1
                if self.defs2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'final'}:
            if self.TS[self.index].CP == 'final':
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'interface'}:
            if self.TS[self.index].CP == 'interface':
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'enum'}:
            if self.enum_def():
                if self.defs():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'$'}:
            # Epsilon production
            return True
        return False

    def MST(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT', 'String', 'dict', 'TS', 'ID', 'if', 'while', 'try', 'throw', 'flowControl'}:
            if self.SST():
                if self.MST():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'return', ')'}:
            # Epsilon production
            return True
        return False

    def return_st(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'return'}:
            if self.TS[self.index].CP == 'return':
                self.index += 1
                if self.OE():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {')'}:
            # Epsilon production
            return True
        return False

    def func_def(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.fnd2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'String'}:
            if self.TS[self.index].CP == 'String':
                self.index += 1
                if self.fnd2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'void'}:
            if self.TS[self.index].CP == 'void':
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.fnd2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'dict'}:
            if self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.fnd2():
                    return True
        return False

    def extends_st(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'extends'}:
            if self.TS[self.index].CP == 'extends':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'implements', ':'}:
            # Epsilon production
            return True
        return False

    def implements_st(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'implements'}:
            if self.TS[self.index].CP == 'implements':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.interface_rec():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {':'}:
            # Epsilon production
            return True
        return False

    def class_body(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'AM'}:
            if self.TS[self.index].CP == 'AM':
                self.index += 1
                if self.cb3():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'static'}:
            if self.TS[self.index].CP == 'static':
                self.index += 1
                if self.amh3():
                    if self.cb2():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'final'}:
            if self.TS[self.index].CP == 'final':
                self.index += 1
                if self.cb2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'DT', 'String', 'dict', 'ID', 'void'}:
            if self.cb2():
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {')'}:
            # Epsilon production
            return True
        return False

    def defs2(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'final', 'class'}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'interface'}:
            if self.TS[self.index].CP == 'interface':
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
        return False

    def extends_st_interface(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'extends'}:
            if self.TS[self.index].CP == 'extends':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.interface_rec():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {':'}:
            # Epsilon production
            return True
        return False

    def interface_body(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'AM'}:
            if self.TS[self.index].CP == 'AM':
                print("hahahha")
                self.index += 1
                if self.ifb2():
                    print("fb2 se agae")
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'DT'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.ifb3():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'String'}:
            if self.TS[self.index].CP == 'String':
                self.index += 1
                if self.ifb3():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.ifb4():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'dict'}:
            if self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.ifb5():
                    return True
        return False

    def enum_def(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'enum'}:
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
        return False

    def SST(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec1():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'String'}:
            if self.TS[self.index].CP == 'String':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec1():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'dict'}:
            if self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec3():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'TS'}:
            if self.TS[self.index].CP == 'TS':
                self.index += 1
                if self.TS[self.index].CP == '.':
                    self.index += 1
                    if self.TS[self.index].CP == 'ID':
                        self.index += 1
                        if self.option():
                            if self.SST2():
                                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.SST_prime():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'if'}:
            if self.ifelse_st():
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'while'}:
            if self.while_st():
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'flowcontrol'}:
            if self.TS[self.index].CP == 'flowControl':
                self.index += 1
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'try'}:
            if self.trycatch_st():
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'throw'}:
            if self.throw_st():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    return True
        return False

    def fnd2(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
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
        return False

    def params_list(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT', 'ID', 'String', 'dict'}:
            if self.params():
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}'}:
            # Epsilon production
            return True
        return False

    def params(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.params2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.params2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'String'}:
            if self.TS[self.index].CP == 'String':
                self.index += 1
                if self.params2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'dict'}:
            if self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.params2():
                    return True
        return False

    def params2(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.list_param():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
                self.index += 1
                if self.TS[self.index].CP == ']':
                    self.index += 1
                    if self.arr_mul():
                        if self.TS[self.index].CP == 'ID':
                            self.index += 1
                            if self.list():
                                return True
        return False

    def list_param(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {','}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.params():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}'}:
            # Epsilon production
            return True
        return False

    def arr_mul(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
                self.index += 1
                if self.TS[self.index].CP == ']':
                    self.index += 1
                    if self.arr_mul():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            return True
        return False

    def interface_rec(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {','}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.interface_rec():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {':'}:
            # Epsilon production
            return True
        return False

    def cb3(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.cb2a():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'String'}:
            if self.TS[self.index].CP == 'String':
                self.index += 1
                if self.cb2a():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'dict'}:
            if self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.cb2b():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.cb3a():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'void'}:
            if self.TS[self.index].CP == 'void':
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'static'}:
            if self.TS[self.index].CP == 'static':
                self.index += 1
                if self.amh3():
                    if self.cb2():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'final'}:
            if self.TS[self.index].CP == 'final':
                self.index += 1
                if self.cb2():
                    return True
        return False

    def amh3(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'final'}:
            if self.TS[self.index].CP == 'final':
                self.index += 1
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'DT', 'String', 'dict', 'ID', 'void'}:
            # Epsilon production
            return True
        return False

    def cb2(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.cb2a():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.cb2c():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'String'}:
            if self.TS[self.index].CP == 'String':
                self.index += 1
                if self.cb2a():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'void'}:
            if self.TS[self.index].CP == 'void':
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'dict'}:
            if self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.cb2b():
                    return True
        return False

    def ch2(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'final'}:
            if self.TS[self.index].CP == 'final':
                self.index += 1
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'class'}:
            # Epsilon production
            return True
        return False

    def cb2a(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.cb2a1():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
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
        return False

    def cb2b(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.cb2b1():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
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
        return False

    def cb3a(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID', '['}:
            if self.cb2c():
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
            if self.TS[self.index].CP == '{':
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
        return False

    def cb2c(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.cb2c1():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
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
        return False

    def cb2a1(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', '[', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', ','}:
            if self.dec1():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.class_body():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
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
        return False

    def cb2b1(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', '[', ',', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void'}:
            if self.dec3():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.class_body():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
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
        return False

    def cb2c1(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', '[', ',', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void'}:
            if self.dec2():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.class_body():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
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
        return False

    def dec1(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', ','}:
            if self.init_var():
                if self.list_var():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == ']':
                        self.index += 1
                        if self.arr_size():
                            if self.init_arr():
                                if self.list_arr():
                                    return True
        return False

    def dec2(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', ','}:
            if self.init():
                if self.list():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == ']':
                        self.index += 1
                        if self.arr_size():
                            if self.init_arr():
                                if self.list_arr():
                                    return True
        return False

    def dec3(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', ','}:
            if self.init_dict():
                if self.list_dict():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == ']':
                        self.index += 1
                        if self.arr_size():
                            if self.init_arr():
                                if self.list_arr():
                                    return True
        return False

    def init_var(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'='}:
            if self.TS[self.index].CP == '=':
                self.index += 1
                if self.OE():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {',', 'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return'}:
            # Epsilon production
            return True
        return False

    def list_var(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {','}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.init_var():
                        if self.list_var():
                            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return'}:
            # Epsilon production
            return True
        return False

    def arr_size(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == ']':
                        self.index += 1
                        if self.arr_size():
                            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'=', ',', 'AM', 'static', 'final', 'string', 'DT', 'ID', 'dict', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return'}:
            # Epsilon production
            return True
        return False

    def init_arr(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'='}:
            if self.TS[self.index].CP == '=':
                self.index += 1
                if self.init_arr_b():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'AM', 'static', 'final', 'string', 'DT', 'ID', 'dict', 'void',',', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return'}:
            # Epsilon production
            return True
        return False

    def list_arr(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {','}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return'}:
            # Epsilon production
            return True
        return False

    def init_arr_b(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.init_arr():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.value_list():
                return True
        return False

    def value_list(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
                self.index += 1
                if self.values():
                    if self.TS[self.index].CP == ']':
                        self.index += 1
                        return True
        return False

    def values(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', '{', 'TS', 'ID'}:
            if self.OE():
                if self.arr_val_values_prime():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.value_list():
                if self.arr_val_values_prime():
                    return True
        return False

    def arr_val_values_prime(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {','}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.values():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {']'}:
            # Epsilon production
            return True
        return False

    def init(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'='}:
            if self.TS[self.index].CP == '=':
                self.index += 1
                if self.init2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return', ','}:
            # Epsilon production
            return True
        return False

    def init2(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'new'}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', '{', 'TS', 'ID'}:
            if self.OE():
                return True
        return False

    def list(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {','}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.list2():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return'}:
            # Epsilon production
            return True
        return False

    def list2(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {',', 'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return'}:
            if self.init():
                if self.list():
                    return True
        return False

    def init_dict(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'='}:
            if self.TS[self.index].CP == '=':
                self.index += 1
                if self.init_dict_b():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return', ','}:
            # Epsilon production
            return True
        return False

    def init_dict_b(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.init_dict():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
            if self.TS[self.index].CP == '{':
                self.index += 1
                if self.values_of_dic():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        return True
        return False

    def values_of_dic(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.TS[self.index].CP == ':':
                    self.index += 1
                    if self.OE():
                        if self.dict_val():
                            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}'}:
            # Epsilon production
            return True
        return False

    def list_dict(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {','}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.init_dict():
                        if self.list_dict():
                            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return', ','}:
            # Epsilon production
            return True
        return False

    def dict_val(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {','}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == ':':
                        self.index += 1
                        if self.OE():
                            if self.dict_val():
                                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}'}:
            # Epsilon production
            return True
        return False

    def constr_body(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'TS'}:
            if self.TS[self.index].CP == 'TS':
                self.index += 1
                if self.constr_body2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'DT'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec1():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.MST():
                                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'String'}:
            if self.TS[self.index].CP == 'String':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec1():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.MST():
                                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'dict'}:
            if self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec3():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.MST():
                                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.SST_prime():
                    if self.MST():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'if'}:
            if self.ifelse_st():
                if self.MST():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'whie'}:
            if self.while_st():
                if self.MST():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'flowcontrol'}:
            if self.TS[self.index].CP == 'flowControl':
                self.index += 1
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.MST():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'try'}:
            if self.trycatch_st():
                if self.MST():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'throw'}:
            if self.throw_st():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.MST():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {')'}:
            # Epsilon production
            return True
        return False

    def constr_body2(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'.'}:
            if self.TS[self.index].CP == '.':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.option():
                        if self.SST2():
                            if self.MST():
                                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
            if self.TS[self.index].CP == '{':
                self.index += 1
                if self.args_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.MST():
                                return True
        return False

    def args_list(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'L01', '{', 'TS', 'ID'}:
            if self.OE():
                if self.list_args():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}'}:
            # Epsilon production
            return True
        return False

    def list_args(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {','}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.OE():
                    if self.list_args():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}'}:
            # Epsilon production
            return True
        return False

    def ifb2(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'static'}:
            if self.TS[self.index].CP == 'static':
                self.index += 1
                if self.TS[self.index].CP == 'final':
                    self.index += 1
                    if self.dec():
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.interface_body():
                                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'DT', 'String', 'ID', 'dict'}:
            if self.func_def_interface():
                if self.interface_body():
                    return True
        return False

    def ifb3(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.ifb3a():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
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
        return False

    def ifb3a(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', '[', ','}:
            if self.dec1():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.interface_body():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
            if self.TS[self.index].CP == '{':
                self.index += 1
                if self.params_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.interface_body():
                                return True
        return False

    def ifb4(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.ifb4a():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
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
        return False

    def ifb4a(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', '[', ','}:
            if self.dec2():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.interface_body():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
            if self.TS[self.index].CP == '{':
                self.index += 1
                if self.params_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.interface_body():
                                return True
        return False

    def ifb5(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.ifb5a():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
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
        return False

    def ifb5a(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', '[', ','}:
            if self.dec3():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.interface_body():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
            if self.TS[self.index].CP == '{':
                self.index += 1
                if self.params_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            if self.interface_body():
                                return True
        return False

    def dec(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec1():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'String'}:
            if self.TS[self.index].CP == 'String':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec1():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec2():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'dict'}:
            if self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec3():
                        return True
        return False

    def func_def_interface(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT'}:
            if self.TS[self.index].CP == 'DT':
                print("hahahah")
                self.index += 1
                print("index brh")
                if self.fn_def_inter2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'String'}:
            if self.TS[self.index].CP == 'String':
                self.index += 1
                if self.fn_def_inter2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.fn_def_inter2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'dict'}:
            if self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.fn_def_inter2():
                    return True
        return False

    def fn_def_inter2 (self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.TS[self.index].CP == '{':
                    self.index += 1
                    print("curly match")
                    if self.params_list():
                        if self.TS[self.index].CP == '}':
                            self.index += 1
                            if self.TS[self.index].CP == 'ln':
                                self.index += 1
                                return True
            elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
                if self.TS[self.index].CP == '[':
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
            return False


    def enum_list(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {','}:
            if self.TS[self.index].CP == ',':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.init_enum_def():
                        if self.enum_list():
                            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {')'}:
            # Epsilon production
            return True
        return False

    def init_enum_def(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'='}:
            if self.TS[self.index].CP == '=':
                self.index += 1
                if self.OE():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {')', ','}:
            # Epsilon production
            return True
        return False

    def option(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'}', ')', ']', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2', 'RO1', 'RO2', 'PM', 'MDME', '=', 'COMPASS', 'instanceof', ','}:
            # Epsilon production
            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'.'}:
            if self.TS[self.index].CP == '.':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.option():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'['}:
            if self.TS[self.index].CP == '[':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == ']':
                        self.index += 1
                        if self.option():
                            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'('}:
            if self.TS[self.index].CP == '(':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == ')':
                        self.index += 1
                        if self.option():
                            return True   
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
            if self.TS[self.index].CP == '{':
                self.index += 1
                if self.args_list():
                    if self.TS[self.index].CP == '}':
                        self.index += 1
                        if self.option2():
                            return True
        return False

    def option2(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'.'}:
            if self.TS[self.index].CP == '.':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.option():
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ln'}:
            if self.TS[self.index].CP == 'ln':
                self.index += 1
                return True
        return False

    def SST2(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ln'}:
            if self.TS[self.index].CP == 'ln':
                self.index += 1
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'='}:
            if self.TS[self.index].CP == '=':
                self.index += 1
                if self.SST3():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'COMPASS'}:
            if self.TS[self.index].CP == 'COMPASS':
                self.index += 1
                if self.OE():
                    if self.TS[self.index].CP == 'ln':
                        self.index += 1
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'instanceof'}:
            if self.TS[self.index].CP == 'instanceof':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == 'ln':
                        self.index += 1
                        return True
        return False

    def SST3(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', '{', 'TS', 'ID'}:
            if self.OE():
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'new'}:
            if self.TS[self.index].CP == 'new':
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
        return False

    def SST_prime(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'.', '[', '(', '{', '=', 'COMPASS', 'instanceof', 'DT', 'String', 'dict', 'ID', }:
            if self.option():
                if self.SST2():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.dec2():
                    if self.TS[self.index].CP == 'ln':
                        self.index += 1
                        return True
        return False

    def ifelse_st(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'if'}:
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
        return False

    def else_if(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'elif'}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'DT', 'String', 'dict', 'TS', 'ID', 'if', 'while', 'try', 'throw', 'flowControl', 'return', ')', 'else'}:
            # Epsilon production
            return True
        return False

    def else_st(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'else'}:
            if self.TS[self.index].CP == 'else':
                self.index += 1
                if self.body():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'DT', 'String', 'dict', 'TS', 'ID', 'if', 'while', 'try', 'throw', 'flowControl', 'return', ')'}:
            # Epsilon production
            return True
        return False

    def while_st(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'while'}:
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
        return False

    def trycatch_st(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'try'}:
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
                                    if self.TS[self.index].CP == 'ID}':
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
        return False

    def throw_st(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'throw'}:
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
        return False

    def body1(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'('}:
            if self.TS[self.index].CP == '(':
                self.index += 1
                if self.MST():
                    if self.return_st():
                        if self.TS[self.index].CP == ')':
                            self.index += 1
                            return True
        return False


