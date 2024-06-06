#!/usr/bin/env python3

import sys
from typing import List


class Token:
    def __init__(self) -> None:
        pass


class Scanner:
    def __init__(self, source) -> None:
        self.source = source

    def scan_tokens(self) -> List[Token]:
        return []


def run(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    for token in tokens:
        print(token)


def run_file(filename):
    with open(filename, mode="r") as f:
        contents = f.read()
    run(contents)


def run_prompt():
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        run(line)


def main():
    args = sys.argv
    if len(args) > 2:
        print(f"Usage: {args[0]} [script]")
        sys.exit(64)
    elif len(args) == 2:
        run_file(args[1])
    else:
        run_prompt()


if __name__ == "__main__":
    main()
