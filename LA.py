from keywords import match_keywords
from operators import match_operators
from punctuators import match_puncutators
import pattern_matcher as pm

class Token:
    def __init__(self, class_part, value_part, line_no):
        self.class_part = class_part
        self.value_part = value_part
        self.line_no = line_no

    def print(self):
        print(self.class_part)
        print(self.value_part)
        print(self.line_no)

def word_break(file : str, index : int, line_no : int):
    temp = ""
    for i in range(index, len(file)):
        if (file[i] == '\n'):
            line_no += 1
            index += 1
            break
        if(file[i] == " "): # word breaker
            index += 1
            break
        temp += file[i]
        index += 1

    return temp, index, line_no

def validate_word(word): # on working
    # print(word)

    cp = pm.match_ID(word)
    if cp:
        return cp

    cp = match_keywords(word)
    if cp:
        return cp

    cp = match_operators(word)
    if cp:
        return cp

    cp = match_puncutators(word)
    if cp:
        return cp

    cp = pm.match_string_const(word)
    if cp:
        return cp

    cp = pm.match_char_const(word)
    if cp:
        return cp

    cp = pm.match_number_const(word)
    if cp:
        return cp

    return "Invalid lexene"

def LA (file):
    tokenSet = []
    index = 0
    line_no = 1
    while(index != len(file)):
        temp, index, line_no = word_break(file, index, line_no)
        # print(index)
        class_part = validate_word(temp)
        token = Token(class_part, temp, line_no)
        tokenSet.append(token)

    return tokenSet


file = open('word.txt', 'rt')
# src = file.readlines()
src = file.read()
file.close()
# print(src[0].find('\n'))
# print(file)
tokenSet = LA(src)
for token in tokenSet:
    token.print()