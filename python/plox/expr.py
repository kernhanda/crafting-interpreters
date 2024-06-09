from typing import Any

from python.plox.token import Token


class Expr:
    def __init__(self) -> None:
        pass


class Binary(Expr):
    def __init__(self, left: Expr, op: Token, right: Expr) -> None:
        super().__init__()
        self.left = left
        self.op = op
        self.right = right


class Grouping(Expr):
    def __init__(self, expr: Expr) -> None:
        super().__init__()
        self.expr = expr


class Literal(Expr):
    def __init__(self, value: Any) -> None:
        super().__init__()
        self.value = value


class Unary(Expr):
    def __init__(self, op: Token, right: Expr) -> None:
        super().__init__()
        self.op = op
        self.right = right
