import re

def check_pattern(word):
    # Patterns for different types of constants
    identifier_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'  # Write your regex for identifier
    string_constant_pattern = r'^"[^"]*"$'  # Write your regex for string constant
    number_constant_pattern = r'^\d+(\.\d+)?$'  # Write your regex for number constant
    char_constant_pattern = r'^\'[^\']\''  # Write your regex for char constant
    
    # Dictionary to store patterns and their names
    patterns = {
        'Identifier': identifier_pattern,
        'String Constant': string_constant_pattern,
        'Number Constant': number_constant_pattern,
        'Character Constant': char_constant_pattern
    }
    
    matches = []
    # Check each pattern
    for pattern_name, pattern in patterns.items():
        if pattern and re.fullmatch(pattern, word):
            matches.append(pattern_name)
    
    return matches

def main():
    while True:
        # Get input from user
        word = input("\nEnter a word to check (or 'quit' to exit): ")
        
        if word.lower() == 'quit':
            print("Exiting program...")
            break
        
        # Check the word against patterns
        matched_patterns = check_pattern(word)
        
        # Display results
        if matched_patterns:
            print(f"'{word}' matches the following pattern(s):")
            for pattern in matched_patterns:
                print(f"- {pattern}")
        else:
            print(f"'{word}' doesn't match any of the defined patterns")

if __name__ == "__main__":
    print("Pattern Matcher Program")
    print("Enter 'quit' to exit the program")
    main()