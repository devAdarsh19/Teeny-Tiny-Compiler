from lex import *

if __name__ == '__main__':
    source = 'LET foobar = 123'
    lexer = Lexer(source)
    
    while lexer.peek() != '\0':
        print(lexer.curChar)
        lexer.nextChar()