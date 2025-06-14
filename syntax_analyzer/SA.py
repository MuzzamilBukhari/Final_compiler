
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
                print("In S, Invalid Syntax at line no : ", self.TS[self.index].line_no)
        else:
            print("Invalid Syntax at line no : ", self.TS[self.index].line_no, "Value part", self.TS[self.index-2].VP)
            print("Invalid Syntax at line no : ", self.TS[self.index].line_no, "Value part", self.TS[self.index-1].VP)
            print("Invalid Syntax at line no : ", self.TS[self.index].line_no, "Value part", self.TS[self.index].VP)

    def OE(self):
        if self.AE():
            print("AE se agya")
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
            print("RE2 se agaya")
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
            print("a")
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
            print("a")
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
            print("a")
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
            print("f")
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
        print(self.TS[self.index].CP)
        if self.index < len(self.TS) and self.TS[self.index].CP in {'str_const', 'num_const', 'char_const', 'bool_const', 'null_const'}:
            print("str conts again")
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
            if self.TS[self.index].CP == 'LO1':
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
                        if self.opt():
                            if self.F1():
                                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            print("ID match hogai")
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                if self.opt():
                    print("option se agya")
                    print(self.TS[self.index].CP)
                    if self.F1():
                        print("F1 se agya")
                        return True
        return False
    
    def opt(self):  
        pass
    
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
        if self.index < len(self.TS) and self.TS[self.index].CP in {'}', ')', ']', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2', 'RO1', 'RO2', 'PM', 'MDME', ','}:
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
                                        print("body1 se agya")
                                        if self.defs():
                                            print("defs se agya")
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
                    print("MST se agya")
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
            print("class m agya")
            if self.TS[self.index].CP == 'class':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.extends_st():
                        print("Extends se agya")
                        if self.implements_st():
                            print("implements se agya")
                            if self.TS[self.index].CP == ':':
                                self.index += 1
                                if self.TS[self.index].CP == '(':
                                    print("( se agya")
                                    self.index += 1
                                    if self.class_body():
                                        print("class body se agya")
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
            print("interface m agya")
            if self.TS[self.index].CP == 'interface':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    print("ID se agya")
                    if self.extends_st_interface():
                        print("extends se agya")
                        if self.TS[self.index].CP == ':':
                            self.index += 1
                            if self.TS[self.index].CP == '(':
                                self.index += 1
                                print("interface body me jaega")
                                if self.interface_body():
                                    print("interface body se agya")
                                    if self.TS[self.index].CP == ')':
                                        self.index += 1
                                        if self.defs():
                                            print("defs se agya")
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
        print("MST me agya")
        print(self.TS[self.index].CP)
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT', 'String', 'dict', 'TS', 'ID', 'if', 'while', 'try', 'throw', 'flowControl'}:
            print("MST ID se agya")
            if self.SST():
                print("SST se agya")
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
                if self.NEXT():
                    print("NEXT se agya")
                    if self.TS[self.index].CP == 'ln':
                        self.index += 1
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {')'}:
            # Epsilon production
            return True
        return False

    def NEXT(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {  'str_const', 'num_const', 'char_const', 'bool_const', 'null_const', 'LO1', '{', 'TS', 'ID' }:
            if self.OE():
                print("OE se agya")
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ln'}:
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
        print("extends_st me agya")
        print(self.TS[self.index].CP)
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
            print("cb2 me jaega")
            if self.cb2():
                print("cb2 sea gya")
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
                        print(self.TS[self.index].CP)
                        if self.extends_st():
                            print("extends se agya")
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
                    print("ifb2 se agae")
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'DT'}:
            if self.TS[self.index].CP == 'DT':
                print("DT se agya")
                self.index += 1
                if self.ifb3():
                    print("ifb3 se agae")
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {')'}:
            if self.TS[self.index].CP == ')':
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
        print("SST me agya")
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
                        print("dec1 se agae")
                        if self.TS[self.index].CP == 'ln':
                            self.index += 1
                            return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'dict'}:
            if self.TS[self.index].CP == 'dict':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.dec3():
                        print(self.TS[self.index].CP)
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
                print("SST ID se agya")
                if self.SST_prime():
                    print("SST prime se agya")
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'if'}:
            if self.ifelse_st():
                print("if else se agya")
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'while'}:
            if self.while_st():
                return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'flowControl'}:
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
            print("Idhr")
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
                print("param ki ID se agya")
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
        print("cb2 me agya")
        print(self.TS[self.index].CP)
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT'}:
            if self.TS[self.index].CP == 'DT':
                self.index += 1
                if self.cb2a():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                print("cb2c me jaega")
                if self.cb2c():
                    print("cb2c se agya")
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'String'}:
            print("string match krega ")
            if self.TS[self.index].CP == 'String':
                self.index += 1
                print("cb2a me jaega")
                if self.cb2a():
                    print("cb2a se agya")
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'void'}:
            if self.TS[self.index].CP == 'void':
                self.index += 1
                if self.TS[self.index].CP == 'ID':
                    self.index += 1
                    if self.TS[self.index].CP == '{':
                        self.index += 1
                        if self.params_list():
                            print("param se agya")
                            if self.TS[self.index].CP == '}':
                                self.index += 1
                                if self.TS[self.index].CP == ':':
                                    self.index += 1
                                    if self.body():
                                        print("body se agya")
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
                print("cb2a1 me jaega")
                if self.cb2a1():
                    print("cb2a1 se agya")
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
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', '[', ',', 'ln'}:
            if self.dec1():
                print("dec1 se wapis")
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
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', '[', ',', 'ln'}:
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
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', '[', ',', 'ln'}:
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
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', ',' , 'AM' , 'String' , 'DT' , 'ID' , 'dict' , 'static' , 'final' , 'void' ,  ')' , 'TS' , 'if' , 'while' , 'try' , 'throw' , 'flowControl' , 'return' , 'ln'}:
            if self.init_var():
                print("init_var se agya")
                if self.list_var():
                    print("list_var se agya")
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
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', ',' , 'AM' , 'String' , 'DT' , 'ID' , 'dict' , 'static' , 'final' , 'void' ,  ')' , 'TS' , 'if' , 'while' , 'try' , 'throw' , 'flowControl' , 'return' , 'ln'}:
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
        print("dec3 me agya")
        print(self.TS[self.index].CP)
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', ',' , 'AM' , 'String' , 'DT' , 'ID' , 'dict' , 'static' , 'final' , 'void' ,  ')' , 'TS' , 'if' , 'while' , 'try' , 'throw' , 'flowControl' , 'return' , 'ln'}:
            if self.init_dict():
                print("init_dict se agya")
                if self.list_dict():
                    print("list_dict se agya")
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
                    print("OE se agya")
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ln', ',', 'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return'}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return', 'ln'}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ln','=', ',', 'AM', 'static', 'final', 'string', 'DT', 'ID', 'dict', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return'}:
            # Epsilon production
            return True
        return False

    def init_arr(self):
        if self.index < len(self.TS) and self.TS[self.index].CP in {'='}:
            if self.TS[self.index].CP == '=':
                self.index += 1
                if self.init_arr_b():
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ln','AM', 'static', 'final', 'string', 'DT', 'ID', 'dict', 'void',',', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return'}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ln', 'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return'}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ln','AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return', ','}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ln', 'AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return'}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ln','AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return', ','}:
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
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'ln','AM', 'String', 'DT', 'ID', 'dict', 'static', 'final', 'void', ')', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return', ','}:
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
            print("str const uthalia")
            if self.OE():
                print("OE se agya")
                if self.list_args():
                    print("list args se aagya")
                    return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'}'}:
            # Epsilon production
            return True
        return False

    def list_args(self):
        print("list args me agya")
        if self.index < len(self.TS) and self.TS[self.index].CP in {','}:
            print("comma match")
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
                print("ID se agya")
                self.index += 1
                if self.ifb3a():
                    print("ifb3a se agya")
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
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', '[', ',', 'ln'}:
            if self.dec1():
                print("dec1 se agya")
                if self.TS[self.index].CP == 'ln':
                    self.index += 1
                    if self.interface_body():
                        print("interfac body se agya")
                        return True
        elif self.index < len(self.TS) and self.TS[self.index].CP in {'{'}:
            if self.TS[self.index].CP == '{':
                self.index += 1
                if self.params_list():
                    print("paramslist se agya")
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
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', '[', ',', 'ln'}:
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
        if self.index < len(self.TS) and self.TS[self.index].CP in {'=', '[', ',', 'ln'}:
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
        print("fn_def_inter2")
        if self.index < len(self.TS) and self.TS[self.index].CP in {'ID'}:
            if self.TS[self.index].CP == 'ID':
                self.index += 1
                print("ID match")
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
        if self.index < len(self.TS) and self.TS[self.index].CP in {'}', ')', ']', 'AM', 'static', 'final', 'DT', 'String', 'dict', 'ID', 'void', 'ln', 'LO3', 'LO2', 'RO1', 'RO2', 'PM', 'MDME', '=', 'COMPASS', 'instanceof', ',', 'TS', 'if', 'while', 'try', 'throw', 'flowControl', 'return', ')'}:
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
            print("option se { ye lelia")
            if self.TS[self.index].CP == '{':
                print("option se { ye lelia")
                self.index += 1
                if self.args_list():
                    print("args list se agya")
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
        if self.index < len(self.TS) and self.TS[self.index].CP in {'DT','String','dict','TS','ID','if','while','try','throw','flowControl','return',')'}:
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
        print("SST_prime me agya")
        print(self.TS[self.index].VP)
        if self.index < len(self.TS) and self.TS[self.index].CP in { '.','[', '{', '(', 'ln', '=', 'COMPASS', 'instanceof' }:
            print("SST_prime me if se agya")
            if self.option():
                print("option se agya")
                print(self.TS[self.index].CP)
                if self.SST2():
                    print("SST2 se agya")
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
        print("else_if me agya")
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
        print("else me agae")
        if self.index < len(self.TS) and self.TS[self.index].CP in {'else'}:
            if self.TS[self.index].CP == 'else':
                self.index += 1
                print("else ke aage")
                if self.body():
                    print("else body se agya")
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
                        print("try body se agya")
                        if self.TS[self.index].CP == 'catch':
                            self.index += 1
                            print("catch")
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


