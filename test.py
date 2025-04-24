# import keywords

# print('let' in keywords.keywords)

# val='3433' 
# print(val.isdigit()) # is method se ham string me integers ko check krsaty hen!


# #  if char == '~':
# #             if temp:  
# #                 return temp, index, line_no  # Pehle temp return karo
# #             while index < len(file) and file[index] != '\n':
# #                 index += 1  # Comment ke characters skip karo
# #             index += 1  # Newline bhi skip kar do
# #             continue  # Agla character process karo

# # a = "r
# # a += alkdlk
# a = r"abc\n"
# print(a)

parser_code = ""

parser_code += "class Parser:\n"
parser_code += "    def __init__(self, tokens):\n"
parser_code += "        self.tokens = tokens\n"
parser_code += "        self.pos = 0\n\n"
parser_code += "    def current_token(self):\n"
parser_code += "        if self.pos < len(self.tokens):\n"
parser_code += "            return self.tokens[self.pos]['classpart']\n"
parser_code += "        return '$'\n\n"
parser_code += "    def match(self, expected):\n"
parser_code += "        if self.current_token() == expected:\n"
parser_code += "            self.pos += 1\n"
parser_code += "        else:\n"
parser_code += "            raise SyntaxError(f\"Expected {expected} but found {self.current_token()}\")\n\n"
print(parser_code)