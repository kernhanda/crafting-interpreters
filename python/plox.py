#!/usr/bin/env python3

import sys

from plox import *
from plox import LoxError, Scanner


def run(source: str):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    for token in tokens:
        print(token)


def run_file(filename: str):
    with open(filename, mode="r") as f:
        contents = f.read()
    run(contents)


def run_prompt():
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        try:
            run(line)
        except LoxError:
            pass


def main():
    expr = Binary(
        Unary(Token(TokenType.MINUS, "-", None, 1), Literal(123)),
        Token(TokenType.STAR, "*", None, 1),
        Grouping(Literal(45.67)),
    )
    print(AstPrinter().print(expr))
    return

    args = sys.argv
    if len(args) > 2:
        print(f"Usage: {args[0]} [script]")
        sys.exit(64)
    elif len(args) == 2:
        try:
            run_file(args[1])
        except LoxError:
            sys.exit(65)
    else:
        run_prompt()


if __name__ == "__main__":
    main()
