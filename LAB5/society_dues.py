"""Manage society dues, payments, late fees, and pending collections."""

import sqlite3
import ast
import operator

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE dues (flat TEXT, month TEXT, amount INTEGER, paid INTEGER)"
)


def add_due(flat, month, amount, history=None):
    """Add a society due record and update the collection history."""
    if history is None:
        history = []

    conn.execute(
    "INSERT INTO dues VALUES (?, ?, ?, 0)",
    (flat, month, amount),
    )
    history.append((flat, month))
    return history


def collect(flat, month):
    """Mark a flat's monthly dues as paid and return the amount."""
    row = conn.execute(
        "SELECT amount FROM dues WHERE flat = ? AND month = ?",
        (flat, month),
    ).fetchone()

    if row:
        conn.execute(
            "UPDATE dues SET paid = 1 WHERE flat = ? AND month = ?",
            (flat, month),
        )
        return row[0]

    return None


def evaluate_arithmetic(expression):
    """Evaluate a restricted arithmetic expression without executing Python code."""
    if not isinstance(expression, str) or len(expression) > 100:
        raise ValueError("Invalid arithmetic expression")

    tree = ast.parse(expression, mode="eval")

    if sum(1 for _ in ast.walk(tree)) > 50:
        raise ValueError("Expression is too complex")

    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    def calculate(node):
        if isinstance(node, ast.Expression):
            return calculate(node.body)

        if isinstance(node, ast.Constant):
            if type(node.value) not in (int, float):
                raise ValueError("Only numeric values are allowed")
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operators:
            if isinstance(node.op, ast.Pow):
                exponent = calculate(node.right)
                if abs(exponent) > 10:
                    raise ValueError("Exponent is too large")
                left = calculate(node.left)
                return operators[type(node.op)](left, exponent)

            left = calculate(node.left)
            right = calculate(node.right)
            return operators[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp) and type(node.op) in operators:
            return operators[type(node.op)](calculate(node.operand))

        raise ValueError("Unsupported arithmetic expression")

    return calculate(tree)


def penalty(rule):
    """Calculate a late fee using restricted arithmetic operations."""
    try:
        return evaluate_arithmetic(rule)
    except (
        SyntaxError,
        ValueError,
        TypeError,
        ZeroDivisionError,
        OverflowError,
    ):
        return 0


def pending():
    """Return the flat numbers whose dues are still unpaid."""
    rows = conn.execute(
        "SELECT flat FROM dues WHERE paid = 0"
    ).fetchall()

    if rows is not None:
        return [row[0] for row in rows]

    return []


def main():
    """Run a small demonstration of the society dues operations."""
    add_due("A-101", "Oct", 2500)
    add_due("A-102", "Oct", 2500)
    print(collect("A-101", "Oct"))
    print(penalty("50 * 2"))
    print(pending())


if __name__ == "__main__":
    main()
