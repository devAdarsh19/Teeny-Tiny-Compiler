# Lexer: Component 1 of 3 in Teeny Tiny Compiler

import enum

class Lexer:
    def __init__(self, source):
        # source is a string
        
        # Adding a newline character so when my compiler encounters one, it understands that the statement has ended
        self.source = source + '\n' 
        self.curChar = ''
        self.curPos = -1
        self.nextChar()
    
    # Process the next char
    def nextChar(self):
        '''
        Description: Increment current position by one. If current position is greater than or equal to length of source, set 
        current character as null character; else, set current character as source[current position].
        '''
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else:
            self.curChar = self.source[self.curPos]
    
    # Return the lookahead character
    def peek(self):
        '''
        Description: If curPos + 1 exceeds length of source, return a null character; else, return the character at curPos + 1
        '''
        if self.curPos + 1 >= len(self.source):
            return '\0'
        else:
            return self.source[self.curPos + 1]
    
    # Print error message for invalid token
    def abort(self, message):
        pass
    
    # Skip whitespace except newlines
    # Newlines will be used to return the end of a statement
    def skipWhitespace(self):
        pass
    
    # Skip comments in code
    def skipComment(self):
        pass
    
    # Return the next token
    def getToken(self):
        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)
        elif self.curChar == '\0':
            token = Token(self.curChar, TokenType.EOF)
        else:
            #unknown token
            pass
    
class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind
        
class TokenType(enum.Enum):
	EOF = -1
	NEWLINE = 0
	NUMBER = 1
	IDENT = 2
	STRING = 3
	# Keywords.
	LABEL = 101
	GOTO = 102
	PRINT = 103
	INPUT = 104
	LET = 105
	IF = 106
	THEN = 107
	ENDIF = 108
	WHILE = 109
	REPEAT = 110
	ENDWHILE = 111
	# Operators.
	EQ = 201  
	PLUS = 202
	MINUS = 203
	ASTERISK = 204
	SLASH = 205
	EQEQ = 206
	NOTEQ = 207
	LT = 208
	LTEQ = 209
	GT = 210
	GTEQ = 211