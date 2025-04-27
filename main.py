import sys
sys.path.append('lexical analyzer')
sys.path.append('syntax analyzer')

from LA import LA
from SA import SA

if __name__ == '__main__':
    file = open('lexical analyzer/test_case.txt', 'rt')
    # src = file.readlines()
    src = file.read()
    file.close()
    tokenSet = LA(src)
    
    for token in tokenSet:
         token.print()
         
    SA(tokenSet)
    
    