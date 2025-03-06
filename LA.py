from keywords import match_keywords
from operators import match_operators
from punctuators import match_puncutators
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
    multi_char_operators = {"!=", "==", "<=", ">=", "+=", "-=", "*=", "/=", "%=", "^="}
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    inside_string = False
    inside_char = False
    string_delimiter = ''

    while index < len(file):
        char = file[index]

        # Handling single-line comment ('#')
        if char == '#':
            if temp:
                return temp, index, line_no
            while index < len(file) and file[index] != '\n':  # Skip comment till newline or end of file
                index += 1
            continue  # Skip processing the comment

        # Handle multi-line comments ('~')
        if char == '~':
            if temp:
                return temp, index, line_no  # Return accumulated token before entering comment mode

            index += 1  # Move past initial '~'
            while index < len(file) and file[index] != '~':  # Look for closing '~'
                if file[index] == '\n':
                    line_no += 1  # Handle line number updates
                index += 1
            
            if index < len(file) and file[index] == '~':  # Skip closing '~'
                index += 1
            continue  # Move to next token

        # Handle string literals (single or double quotes)
        if char in {'"', '`'}:
            if not inside_string and not inside_char:
                inside_string = True
                string_delimiter = char
                temp += char
            elif inside_string and char == string_delimiter:
                inside_string = False
                temp += char
                index += 1
                return temp, index, line_no  # Return string literal
            else:
                temp += char
            index += 1
            continue

        # Handle character literals ('')
        if char == '\'' and not inside_string:
            if not inside_char:
                inside_char = True
                temp += char
            elif inside_char:
                inside_char = False
                temp += char
                index += 1
                return temp, index, line_no  # Return character literal
            index += 1
            continue

        # If inside string or char, continue collecting characters
        if inside_string or inside_char:
            temp += char
            index += 1
            continue

        # Handle floating-point numbers correctly
        if char == '.':
            if temp.isdigit():  # If temp contains a number before '.'
                if index + 1 < len(file) and file[index + 1] in digits:
                    temp += char
                    index += 1
                    continue
                else:
                    return temp, index, line_no  # End number before '.'
            elif not temp:  # If temp is empty, check for floating point
                if index + 1 < len(file) and file[index + 1] in digits:
                    temp += char
                    index += 1
                    continue
                else:
                    return ".", index + 1, line_no  # Return '.' as a separate token
            else:
                return temp, index, line_no  # Break word before '.'

        # If we already have a token and encounter a punctuator, return current token first
        if temp and char in punctuatorsAndSingleOperators:
            return temp, index, line_no  

        # Handle newlines
        if char == '\n':
            line_no += 1
            index += 1
            if temp:
                return temp, index, line_no  # Avoid empty token return
            continue  # Skip newline if temp was empty

        # Handle spaces as word breakers
        if char == " ":
            index += 1
            if temp:
                return temp, index, line_no  # Return collected word
            continue  # Skip space without returning empty token

        # Handle multi-character operators
        if char in {"!", "=", "<", ">", "+", "-", "*", "/", "%", "^"}:
            if index + 1 < len(file):  # Look ahead safely
                next_char = file[index + 1]
                potential_operator = char + next_char
                if potential_operator in multi_char_operators:
                    index += 2  # Move past both characters
                    return potential_operator, index, line_no  # Return operator

        # Handle single-character operators
        if char in punctuatorsAndSingleOperators:
            index += 1
            return char, index, line_no  # Return the operator itself as a token

        # Collect normal characters
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
        tokenSet.append(token)
        # tokenSet.append({ 'value_part': token.value_part,'class_part': token.class_part, 'line_no':token.line_no})
        # tokenSet.append((token.value_part, token.class_part,token.line_no))
    return tokenSet

