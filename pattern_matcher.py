import re

def check_pattern(word):
    # Pattern for identifier: as specified
     # identifier_pattern = r'[a-zA-Z][a-zA-Z0-9][a-zA-Z0-9] | _[a-zA-Z0-9]+ | [a-zA-Z][a-zA-Z0-9][a-zA-Z0-9]_[a-zA-Z0-9]+' # actual regex
    identifier_pattern = r'[a-zA-Z][a-zA-Z0-9]{2}(_[a-zA-Z0-9]+)?|_[a-zA-Z0-9]+'
    
    # Pattern for string constant - allows both " and ` quotes
    string_constant_pattern = r'("[^"]*"|[^]*`)'
    
    # Pattern for number constant - allows optional +/- prefix
    number_constant_pattern = r'[+-]?[0-9]+(\.[0-9]+)?'
    
    # Pattern for character constant - supports escape sequences
    char_constant_pattern = r'\'(\\[ntrb\'\"\\]|[^\'])\''
    
    # Dictionary to store patterns and their names
    patterns = {
        'Identifier': identifier_pattern,
        'String Constant': string_constant_pattern,
        'Number Constant': number_constant_pattern,
        'Character Constant': char_constant_pattern
    }
    
    match_pattern = ""
    # Check each pattern
    for pattern_name, pattern in patterns.items():
        if re.fullmatch(pattern, word):
            match_pattern = pattern_name
    
    return match_pattern

def main():
    while True:
        # Get input from user
        word = input("\nEnter a word to check (or 'quit' to exit): ")
        
        if word.lower() == 'quit':
            print("Exiting program...")
            break
        
        # Check the word against patterns
        matched_pattern = check_pattern(word)
        
        # Display results
        if matched_pattern:
            print(f"'{word}' matches the following pattern : {matched_pattern}")
        else:
            print(f"'{word}' doesn't match any of the defined patterns")

if __name__ == "__main__":
    print("Pattern Matcher Program")
    print("Examples for valid identifiers:")
    print("1. abc    (letter followed by 2 alphanumerics)")
    print("2. abc_123 (letter followed by 2 alphanumerics and underscore part)")
    print("3. _abc    (underscore followed by alphanumerics)")
    print("\nOther examples:")
    print("String constant: \"hello\" or `hello`")
    print("Number constant: 123, -123, +123, 123.456")
    print("Character constant: 'a', '\\n', '\\t', '\\r', '\\b', '\\'', '\\\"', '\\\\'")
    print("\nEnter 'quit' to exit the program")
    main()