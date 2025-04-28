from keywords import match_keywords
from operators import match_operators
from punctuators import match_puncutators
import checking_pattern_matcher as pm

class Token:
    def __init__(self, CP, VP, line_no):
        self.CP = CP
        self.VP = VP
        self.line_no = line_no

    def print(self):
        print(f"Value Part -> {self.VP} | Class Part -> {self.CP} | Line no -> {self.line_no}")
        




def word_break(file: str, index: int, line_no: int):
    temp = r""
    punctuatorsAndSingleOperators = {',', '(', ')', '{', '}', '[', ']', ':', '?', '.', '+', '-', '*', '/', '%', '^', '=', '<', '>', '!', '&', '|'}
    multi_char_operators = {"!=", "==", "<=", ">=", "+=", "-=", "*=", "/=", "%=", "^="}  # Multi-character operators set
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    while index < len(file): 
        char = file[index]
        

        # Handle newlines separately
        if char == '\n':
            if temp:
                return temp, index, line_no  # Avoid returning an empty token
             
            line_no += 1
            index += 1
            return r"\n", index, line_no  # Return newline token before increasing line_no

              

        #     continue  # Move to the next character if temp was empty

        # if char == '\n':
        #         if temp:
        #            return temp, index, line_no  # Return token before handling newline

        #         # temp is empty, so we treat '\n' itself as a token
        #         index += 1
        #         return r"\n", index, line_no  # Return newline token before increasing line_no


        #handling single line comment!
        if char  == '#':
            if temp:
                return temp, index, line_no
            else:
                while(  file[index]!='\n' ):
                    index+=1
                    
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

        
        # Handle spaces as word breakers
        if char == " ":
            if(index + 1 <= len(file)): # last space ko handle krne k lye!
                index += 1
                if temp:
                    return temp, index, line_no  # Return the collected word
                continue  # Skip space without returning an empty token jo bhi beech ki spaces hongi , unko handle krne k lye!
            

        


     
        


        if char == '"' or char == '`':  # Check for string start delimiters
            delimiter = char            # Store which delimiter is used
            if temp:
                return temp, index, line_no  # Return any accumulated token before starting a string
            temp += char                # Append the opening delimiter
            index += 1                  # Skip the opening delimiter

            # Process characters until the closing delimiter is found or file ends
            while index < len(file) and file[index] != delimiter:
                # If an escape sequence is encountered, process it
                if file[index] == "\\":
                    # Ensure there's a next character to escape
                    if index + 1 < len(file):
                        temp += file[index]      # Append the backslash
                        temp += file[index + 1]    # Append the escaped character
                        index += 2               # Skip both characters
                        continue
                    else:
                        temp += file[index]
                        index += 1
                        continue

                # Handle newlines within the string (if needed)
                if file[index] == '\n':
                    temp += r"\n"
                    line_no += 1

                # Append the normal character to the string token
                temp += file[index]
                index += 1

            # If closing delimiter is found, append it and move past it
            if index < len(file) and file[index] == delimiter:
                temp += file[index]
                index += 1

            # Return the full string token including delimiters and escape sequences
            return temp, index, line_no

        
        #handling single quoted chars

        if char == "'":  # Check for single-quote start delimiter
            delimiter = char  # Store the delimiter (')
            if temp:
                return temp, index, line_no  # Return any accumulated token first
            temp += char  # Append the opening delimiter
            index += 1  # Skip the opening delimiter

            count = 0
            while index < len(file) and count < 3:
                if file[index] == '\n':
                    line_no += 1  # Update line number if newline found

                # Escape sequence handling
                if file[index] == '\\' and index + 1 < len(file) and count <= 1:
                    temp += file[index]      # Add backslash
                    temp += file[index + 1]  # Add escaped character
                    index += 2
                    count += 2
                else:
                    temp += file[index]
                    index += 1
                    count += 1

                # Break if closing quote found
                if temp[-1] == delimiter:
                    break

            return temp, index, line_no


        # if char == "'":  # Check for single-quote start delimiter
        #     delimiter = char  # Store the delimiter (')
        #     if temp:
        #         return temp, index, line_no  # Return any accumulated token first
        #     temp += char  # Append the opening delimiter
        #     index += 1  # Skip the opening delimiter

        #     # Process characters until the closing delimiter is found or file ends
        #     while index < len(file) and file[index] != delimiter:
        #         # If an escape sequence is encountered, process it
        #         if file[index] == '\\':
        #             if index + 1 < len(file):
        #                 temp += file[index]      # Append the backslash
        #                 temp += file[index + 1]    # Append the escaped character
        #                 index += 2  # Skip both characters
        #                 continue
        #             else:
        #                 temp += file[index]
        #                 index += 1
        #                 continue

        #         # Handle newlines within the literal (if needed)
        #         if file[index] == '\n':
        #             line_no += 1
        #             return temp, index, line_no

        #         # Append the normal character to the token
        #         temp += file[index]
        #         index += 1

        #     # If the closing delimiter is found, append it and move past it
        #     if index < len(file) and file[index] == delimiter:
        #         temp += file[index]
        #         index += 1

        #     # Return the full token including delimiters and escape sequences
        #     return temp, index, line_no


        # Handle multi-character operators (Lookahead logic)
        if char in {"!", "=", "<", ">", "+", "-", "*", "/", "%", "^"}:
            if index + 1 < len(file):  # Ensure we don't go out of bounds
                next_char = file[index + 1]
                potential_operator = char + next_char

                if potential_operator in multi_char_operators:
                    index += 2  # Move past both characters
                    return potential_operator, index, line_no  # Return multi-character operator

        # If a single-character operator is encountered
        if char in punctuatorsAndSingleOperators: 
            index += 1
            return char, index, line_no  # Return the operator itself as a token

        # Append normal characters to temp
        
        temp += char
        index += 1
    
    return temp, index, line_no  




def validate_word(word : str): 
    # print(word)

    if (word[0] == '_'):
        cp = pm.match_ID(word)
        if cp:
            return cp
        return "Invalid Lexene"

    if (word[0] == '"' or word[0] == '`'):
        cp = pm.match_string_const(word)
        if cp:
            return cp
        return "Invalid Lexene"
    
    if word[0] == "'":
        cp = pm.match_char_const(word)
        if cp:
            return cp
        return "Invalid Lexene"
    
    if (word[0].isdigit() or word[0] == '.'):
        cp = pm.match_number_const(word)
        if cp:
            return cp
        return "Invalid Lexene"
    
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

def LA(file):
    tokenSet = []
    index = 0
    line_no = 1
    while(index != len(file)):
        temp, index, line_no = word_break(file, index, line_no)
        if temp==r"\n":
            CP = validate_word(temp)
            token = Token(CP, temp, line_no-1)
            tokenSet.append(token)

        else:
        # print(index)
            CP = validate_word(temp)
            token = Token(CP, temp, line_no)
            tokenSet.append(token)
        # tokenSet.append({ 'VP': token.VP,'CP': token.CP, 'line_no':token.line_no})
        # tokenSet.append((token.VP, token.CP,token.line_no))
    
    

    # Filter consecutive newline tokens, keeping only one
    filtered_tokenSet = []
    i = 0
    while i < len(tokenSet):
        current_token = tokenSet[i]
        filtered_tokenSet.append(current_token)
        
        # If current token is a newline, skip all consecutive newline tokens
        if current_token.CP == 'ln':
            while i + 1 < len(tokenSet) and tokenSet[i + 1].CP == 'ln':
                i += 1
    
        i += 1

    if filtered_tokenSet[len(filtered_tokenSet) -1].CP == 'ln':
        filtered_tokenSet.pop()
    
    token = Token("$", "", line_no)
    filtered_tokenSet.append(token)
    
    return filtered_tokenSet


