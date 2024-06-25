from functools import singledispatch

from plox.token import Token, TokenType


class LoxError(Exception):
    def __init__(self, line: int, err: str) -> None:
        super().__init__()
        self.line = line
        self.err = err

    def __str__(self) -> str:
        return f"Error at line {self.line}: {self.err}"


@singledispatch
def error(_, message: str):
    assert False


@error.register
def _(line: int, message: str):
    report(line, "", message)


@error.register
def _(token: Token, message: str):
    if token.type == TokenType.EOF:
        report(token.line, " at end", message)
    else:
        report(token.line, f" at '{token.lexeme}'", message)


def report(line: int, where: str, message: str):
    print(f"[line {line}] Error {where}: {message}")
