from keywords import match_keywords
from operators import match_operators
from punctuators import match_puncutators
from checking_pattern_matcher import match_char_const
from checking_pattern_matcher import match_string_const
from checking_pattern_matcher import match_ID
from checking_pattern_matcher import match_number_const
import checking_pattern_matcher as pm

class Token:
    def __init__(self, class_part, value_part, line_no):
        self.class_part = class_part
        self.value_part = value_part
        self.line_no = line_no

    def print(self):
        print(self.class_part)
        print(self.value_part)
        print(self.line_no)




def word_break(file: str, index: int, line_no: int):
    temp = ""
    punctuatorsAndSingleOperators = {',', '(', ')', '{', '}', '[', ']', ':', ';', '?', '.', '+', '-', '*', '/', '%', '^', '=', '<', '>'}
    multi_char_operators = {"!=", "==", "<=", ">=", "+=", "-=", "*=", "/=", "%=", "^="}  # Multi-character operators set
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


    while index < len(file):
        char = file[index]
        
        #handling single line comment!
        if char  == '#':
            if temp:
                return temp, index, line_no
            else:
                while(  file[index]!='\n' ):
                    index+=1
                    continue
            continue

      
# handling multi line comments      

        if char == '~':
    # Agar koi token (temp) already accumulate hua hai, to usko return karo pehle
            if temp:
                return temp, index, line_no

    # Ab hum multi-line comment mode me hain, starting '~' ko skip karo
            index += 1

    # Loop chalao jab tak closing '~' nahi mil jati ya file khatam nahi ho jati
            while index < len(file) and file[index] != '~':
                if file[index] == '\n':
                    line_no += 1  # Har newline pe line number increment karo
                index += 1

    # Agar closing '~' mil jati hai, use bhi skip kar do
            if index < len(file) and file[index] == '~':
                index += 1

    # Comment block complete ho gaya, ab agla token process karne ke liye loop continue karo
            continue

        
                


        # Special handling for '.'
        if char == '.':
            if temp.isdigit():  # Check if temp contains only digits
                # Check next character to confirm it's also a digit
                if index + 1 < len(file) and file[index + 1] in digits:
                    temp += char  # Consider '.' as part of number
                    index+=1
                    continue
                else:
                    return temp, index, line_no  # Break number before '.'
            elif not temp:  # If temp is empty, check next char
                if index + 1 < len(file) and file[index + 1] in digits:
                    temp += char  # Consider '.' as part of floating-point number
                    index+=1
                    continue
                else:
                    return ".", index + 1, line_no  # '.' as separate token
            else:
                return temp, index, line_no  # Break word before '.'




        # If we already have some content in temp and a punctuator is encountered, return the word first
        if temp and char in punctuatorsAndSingleOperators:
            return temp, index, line_no  # Return the word before handling the operator

        # Handle newlines separately
        if char == '\n':
            line_no += 1
            index += 1
            if temp:
                return temp, index, line_no  # Avoid returning an empty token
            continue  # Move to the next character if temp was empty

        # Handle spaces as word breakers
        if char == " ":
            if(index + 1 < len(file)): # last space ko handle krne k lye!
                index += 1
                if temp:
                    return temp, index, line_no  # Return the collected word
                continue  # Skip space without returning an empty token
            

    
       


        # Handle multi-character operators (Lookahead logic)
        if char in {"!", "=", "<", ">", "+", "-", "*", "/", "%", "^"}:
            if index + 1 < len(file):  # Ensure we don't go out of bounds
                next_char = file[index + 1]
                potential_operator = char + next_char

                if potential_operator in multi_char_operators:
                    index += 2  # Move past both characters
                    print("me multi me aaya!", potential_operator )
                    return potential_operator, index, line_no  # Return multi-character operator

        # If a single-character operator is encountered
        if char in punctuatorsAndSingleOperators:
            index += 1
            return char, index, line_no  # Return the operator itself as a token

        # Append normal characters to temp
        temp += char
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
        # tokenSet.append(token)
        # tokenSet.append({ 'value_part': token.value_part,'class_part': token.class_part, 'line_no':token.line_no})
        tokenSet.append((token.value_part, token.class_part,token.line_no))
    return tokenSet


file = open('word.txt', 'rt')
# src = file.readlines()
src = file.read()
file.close()
# print(src[0].find('\n'))
# print(file)
tokenSet = LA(src)
# for token in tokenSet:
#     token.print()
print('tokenSet list=  ',tokenSet)