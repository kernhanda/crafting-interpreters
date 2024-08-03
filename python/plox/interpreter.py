from functools import singledispatchmethod

from plox.expr import *
from plox.token import *
from plox.utils import *


def check_number_operands(operator: Token, *operands: Any):
    if all(map(lambda operand: isinstance(operand, float), operands)):
        return

    raise RuntimeError(operator, "Operand must be a number.")


class Interpreter(Visitor):
    def __init__(self) -> None:
        super().__init__()

    @singledispatchmethod
    def visit(self, _):
        return super().visit(_)

    @visit.register
    def visitBinary(self, expr: Binary):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        match expr.op.type:
            case TokenType.MINUS:
                check_number_operands(expr.op, left, right)
                return left - right
            case TokenType.SLASH:
                check_number_operands(expr.op, left, right)
                return left / right
            case TokenType.STAR:
                check_number_operands(expr.op, left, right)
                return left * right
            case TokenType.PLUS:
                if isinstance(left, str) and isinstance(right, str):
                    return left + right
                if isinstance(left, float) and isinstance(right, float):
                    return left + right
                raise RuntimeError(
                    expr.op, "Operands must be two numbers or two strings"
                )
            case TokenType.GREATER:
                check_number_operands(expr.op, left, right)
                return left > right
            case TokenType.GREATER_EQUAL:
                check_number_operands(expr.op, left, right)
                return left >= right
            case TokenType.LESS:
                check_number_operands(expr.op, left, right)
                return left < right
            case TokenType.LESS_EQUAL:
                check_number_operands(expr.op, left, right)
                return left <= right
            case TokenType.BANG_EQUAL:
                return left != right
            case TokenType.EQUAL_EQUAL:
                return left == right

    @visit.register
    def visitLiteral(self, expr: Literal):
        return expr.value

    @visit.register
    def visitUnary(self, expr: Unary):
        right = self.evaluate(expr.right)

        match expr.op.type:
            case TokenType.MINUS:
                check_number_operands(expr.op, right)
                return -(right)
            case TokenType.BANG:
                return not bool(right)

        assert True, "Should be unreachable"
        return None

    @visit.register
    def visitGrouping(self, expr: Grouping) -> Any | None:
        return self.evaluate(expr.expr)

    def evaluate(self, expr: Expr):
        return expr.accept(self)

    def interpret(self, expr: Expr):
        value = self.evaluate(expr)
        print(str(value))
