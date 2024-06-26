from functools import singledispatchmethod

from plox.expr import *


class Interpreter(Visitor):
    def __init__(self) -> None:
        super().__init__()

    @singledispatchmethod
    def visit(self, _):
        return super().visit(_)

    @visit.register
    def visitBinary(self, expr: Binary): ...

    @visit.register
    def visitLiteral(self, expr: Literal):
        return expr.value

    @visit.register
    def visitUnary(self, expr: Unary): ...

    @visit.register
    def visitGrouping(self, expr: Grouping) -> Any | None:
        return self.evaluate(expr.expr)

    def evaluate(self, expr: Expr):
        return expr.accept(self)
