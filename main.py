from os import sep
import sys
import re

TT_INT = "INT"
TT_PRINTF = "PRINTF"
TT_RETURN = "RETURN"
TT_LBRACKET = "LBRACKET"
TT_RBRACKET = "RBRACKET"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"
TT_SEMICOLON = "SEMICOLON"
TT_QUOTES = "QUOTES"
TT_STRING = "TT_STRING"

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value: return(f"{self.type}: {self.value}")
        return(self.type)

class Lexer:
    def __init__(self, text):
        print(text)
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self, amount=1):
        self.pos += amount 
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def generate_integer_name(self, integer_name):
        while self.current_char != ' ' and self.current_char != '(':
            integer_name += self.current_char
            self.advance()
        return(integer_name)

    def generate_tokens(self):
        tokens = []
        in_string = False
        generating_operator = False
        printing = False
        returning = False

        while self.current_char != None:
            if self.current_char in " \t" or self.current_char in "\n" and not in_string:
                self.advance()
            elif self.current_char == ";":
                tokens.append(Token(TT_SEMICOLON))
                self.advance()
            elif self.current_char == "{":
                tokens.append(Token(TT_LBRACKET))
                self.advance()
            elif self.current_char == "}":
                tokens.append(Token(TT_RBRACKET))
                self.advance()
            elif self.current_char == "(":
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token(TT_RPAREN))
                self.advance()
            elif self.current_char == '"' and not in_string:
                in_string = True
                self.advance()
                string_value = ""
                while self.current_char != '"':
                    string_value += self.current_char
                    self.advance()
                tokens.append(Token(TT_STRING, string_value))
            elif self.current_char == '"' and in_string:
                in_string = False
                self.advance()
            elif self.current_char == 'i' and self.text[self.pos + 1] == 'n' and self.text[self.pos + 2] == 't' and self.text[self.pos + 3] == ' ' and not in_string:
                self.advance(4)
                integer_name = ""
                integer_name = self.generate_integer_name(integer_name)
                tokens.append(Token(TT_INT, integer_name))
            elif self.current_char == 'p' and self.text[self.pos + 1] == 'r' and self.text[self.pos + 2] == 'i' and self.text[self.pos + 3] == 'n' and self.text[self.pos + 4] == 't' and self.text[self.pos + 5] == 'f':
                print(self.current_char)
                self.advance(6)
                printing = True
                #while self.current_char != ")":
                #    print_value += self.current_char
                #    self.advance()
                tokens.append(Token(TT_PRINTF))
                printing = False
            elif self.current_char == 'r' and self.text[self.pos + 1] == 'e' and self.text[self.pos + 2] == 't' and self.text[self.pos + 3] == 'u' and self.text[self.pos + 4] == 'r' and self.text[self.pos + 5] == 'n':
                returning = True
                self.advance(7)
                returning_value = ""
                while self.current_char != ";":
                    returning_value += self.current_char
                    self.advance()
                tokens.append(Token(TT_RETURN, returning_value))
                returning = False
            else:
                self.advance()

        print(tokens)
        return tokens

def main():
    if(len(sys.argv) < 2):
        print("Please provide a file to read")
        return
    file = open(sys.argv[1], "r")

    data = file.read().replace('\n', '')

    lexer = Lexer(data)

    lexer.generate_tokens()


            

if __name__ == "__main__":
    main()