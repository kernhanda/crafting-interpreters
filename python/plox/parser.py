from typing import List

from plox.expr import *
from plox.token import *


class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = tokens
        self.current: int = 0

    def match(self, *types: TokenType) -> bool:
        for t in types:
            if self.check(t):
                self.advance()
                return True

        return False

    def check(self, type: TokenType) -> bool:
        if self.is_at_end():
            return False
        return self.peek().type == type

    def advance(self) -> Token:
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self):
        return self.peek().type == TokenType.EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        assert self.current > 0
        return self.tokens[self.current - 1]

    # expression     → equality ;
    def expression(self) -> Expr:
        return self.equality()

    # equality       → comparison ( ( "!=" | "==" ) comparison )* ;
    def equality(self) -> Expr:
        expr = self.comparison()

        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)

        return expr

    # comparison     → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
    def comparison(self) -> Expr:
        expr = self.term()

        while self.match(
            TokenType.GREATER,
            TokenType.GREATER_EQUAL,
            TokenType.LESS,
            TokenType.LESS_EQUAL,
        ):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)

        return expr

    # term           → factor ( ( "-" | "+" ) factor )* ;
    def term(self) -> Expr:
        expr = self.factor()

        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    # factor         → unary ( ( "/" | "*" ) unary )* ;
    def factor(self) -> Expr:
        expr = self.unary()

        while self.match(TokenType.SLASH, TokenType.STAR):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    # unary          → ( "!" | "-" ) unary
    #                | primary ;
    def unary(self) -> Expr:
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)

        return self.primary()

    # primary        → NUMBER | STRING | "true" | "false" | "nil"
    #                | "(" expression ")" ;
    def primary(self) -> Expr:
        if self.match(TokenType.FALSE):
            return Literal(False)
        if self.match(TokenType.TRUE):
            return Literal(True)
        if self.match(TokenType.NIL):
            return Literal(None)

        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous().literal)

        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)
        raise RuntimeError()
