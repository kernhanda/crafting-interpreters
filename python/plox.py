#!/usr/bin/env python3

import sys

from plox import *
from plox import LoxError, Scanner

interpreter = Interpreter()


def run(source: str):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    try:
        parser = Parser(tokens)
        expression = parser.parse()
    except:
        return

    interpreter.interpret(expression)


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
        except RuntimeError as e:
            print(f"{e}\n[line {e.token.line}]\n")


def main():
    args = sys.argv
    if len(args) > 2:
        print(f"Usage: {args[0]} [script]")
        sys.exit(64)
    elif len(args) == 2:
        try:
            run_file(args[1])
        except LoxError:
            sys.exit(65)
        except RuntimeError:
            sys.exit(70)
    else:
        run_prompt()


if __name__ == "__main__":
    main()
