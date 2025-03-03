import re

def match_ID(word: str):
    """Checks if the given word matches the identifier pattern."""
    identifier_pattern = r'[a-zA-Z][a-zA-Z0-9]{2}(_[a-zA-Z0-9]+)?|_[a-zA-Z0-9]+'
    if bool(re.fullmatch(identifier_pattern, word)):
        return "Identifier"
    else:
        return
    

def match_string_const(word: str):
    """Checks if the given word matches the string constant pattern."""
    string_constant_pattern = r'("(\\[ntbr\'\"\\]|[^"\\])*"|`(\\[ntbr\'\"\\]|[^`\\])*`)'
    if bool(re.fullmatch(string_constant_pattern, word)):
        return "String Constant"
    else:
        return

def match_number_const(word: str):
    """Checks if the given word matches the number constant pattern."""
    number_constant_pattern = r'[+-]?[0-9]+(\.[0-9]+)?'
    if bool(re.fullmatch(number_constant_pattern, word)):
        return "Number Constant"
    else:
        return 

def match_char_const(word: str):
    """Checks if the given word matches the character constant pattern."""
    char_constant_pattern = r'\'(\\[ntrb\'\"\\]|[^\'])\''
    if bool(re.fullmatch(char_constant_pattern, word)):
        return "Char Constant"
    else:
        return 

# def main():
#     print("Pattern Matcher Program for")
#     print("-> Identifier")
#     print("-> String Constant")
#     print("-> Number Constant")
#     print("-> Character Constant")

#     while True:
#         word = input("\nEnter a word to check (or 'quit' to exit): ")
        
#         if word.lower() == 'quit':
#             print("Exiting program...")
#             break

#         print("\nChoose a pattern to check:")
#         print("1. Identifier")
#         print("2. String Constant")
#         print("3. Number Constant")
#         print("4. Character Constant")

#         choice = input("Enter choice (1-4): ")

#         if choice == "1":
#             print(f"'{word}' is a valid Identifier: {match_ID(word)}")
#         elif choice == "2":
#             print(f"'{word}' is a valid String Constant: {match_string_const(word)}")
#         elif choice == "3":
#             print(f"'{word}' is a valid Number Constant: {match_number_const(word)}")
#         elif choice == "4":
#             print(f"'{word}' is a valid Character Constant: {match_char_const(word)}")
#         else:
#             print("Invalid choice. Please enter a number between 1 and 4.")

# if __name__ == "__main__":
#     main()
