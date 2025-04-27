import sys
# Fix path issues by using consistent paths without spaces
sys.path.append('lexical_analyzer')
sys.path.append('syntax_analyzer')

from LA import LA
from SA import SA

if __name__ == '__main__':
    # Fix the file path to use a relative path instead of absolute path
    file = open('syntax_analyzer/test_cases/class.txt', 'rt')
    # src = file.readlines()
    src = file.read()
    file.close()
    tokenSet = LA(src)
    
    for token in tokenSet:
         token.print()

    SA(tokenSet)

