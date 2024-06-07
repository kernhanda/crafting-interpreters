from typing import List

from .token import Token


class Scanner:
    def __init__(self, source) -> None:
        self.source = source

    def scan_tokens(self) -> List[Token]:
        return []
