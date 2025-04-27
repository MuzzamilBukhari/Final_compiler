class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]['classpart']
        return '$'

    def match(self, expected):
        if self.current_token() == expected:
            self.pos += 1
        else:
            raise SyntaxError(f"Expected {expected} but found {self.current_token()}")
