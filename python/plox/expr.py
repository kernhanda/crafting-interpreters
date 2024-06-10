from functools import singledispatchmethod
from typing import Any

from plox.token import Token


class Expr:
    def __init__(self) -> None:
        pass

    def accept(self, visitor: "Visitor") -> Any:
        return visitor.visit(self)


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


class Visitor:
    def __init__(self) -> None:
        pass

    @singledispatchmethod
    def visit(self, _: Expr) -> Any | None:
        pass

    @visit.register
    def visitBinary(self, _: Binary) -> Any | None: ...
    @visit.register
    def visitGrouping(self, _: Grouping) -> Any | None: ...
    @visit.register
    def visitLiteral(self, _: Literal) -> Any | None: ...
    @visit.register
    def visitUnary(self, _: Unary) -> Any | None: ...
