from typing import Any, List, Optional

from python.plox.utils import LoxError

from .token import Token, TokenType


class Scanner:
    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens: List[Token] = []
        self.start: int = 0
        self.current: int = 0
        self.line: int = 1

    def scan_tokens(self) -> List[Token]:
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def advance(self):
        c = self.source[self.current]
        self.current += 1
        return c

    def add_token(self, type: TokenType, literal: Optional[Any] = None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(type, text, literal, self.line))

    def scan_token(self):
        match self.advance():
            case "(":
                self.add_token(TokenType.LEFT_PAREN)
            case ")":
                self.add_token(TokenType.RIGHT_PAREN)
            case "{":
                self.add_token(TokenType.LEFT_BRACE)
            case "}":
                self.add_token(TokenType.RIGHT_BRACE)
            case ",":
                self.add_token(TokenType.COMMA)
            case ".":
                self.add_token(TokenType.DOT)
            case "+":
                self.add_token(TokenType.PLUS)
            case "-":
                self.add_token(TokenType.MINUS)
            case ";":
                self.add_token(TokenType.SEMICOLON)
            case "*":
                self.add_token(TokenType.STAR)
            case _:
                raise LoxError(self.line, "Unexpected character.")
