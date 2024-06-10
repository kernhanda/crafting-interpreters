from functools import singledispatchmethod
from typing import List

from plox.expr import *


class AstPrinter(Visitor):
    def __init__(self) -> None:
        super().__init__()

    @singledispatchmethod
    def visit(self, _):
        return super().visit(_)

    @visit.register
    def visitBinary(self, expr: Binary):
        return self.parenthesize(expr.op.lexeme, expr.left, expr.right)

    @visit.register
    def visitGrouping(self, expr: Grouping):
        return self.parenthesize("group", expr.expr)

    @visit.register
    def visitLiteral(self, expr: Literal):
        return str(expr.value)

    @visit.register
    def visitUnary(self, expr: Unary):
        return self.parenthesize(expr.op.lexeme, expr.right)

    def parenthesize(self, name: str, *exprs: Expr):
        operand_str = ""
        if exprs:
            operand_str = " " + " ".join([expr.accept(self) for expr in exprs])
        return f"({name}{operand_str})"

    def print(self, expr: Expr):
        return expr.accept(self)
