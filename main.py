import sys
sys.path.append('lexical analyzer')

from LA import LA

if __name__ == '__main__':
    file = open('hmara.txt', 'rt')
    # src = file.readlines()
    src = file.read()
    file.close()
    # print(src[0].find('\n'))
    # print(file)
    tokenSet = LA(src)
    for token in tokenSet:
         token.print()
    # print('tokenSet list=  ',tokenSet)