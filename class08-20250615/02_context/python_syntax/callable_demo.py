from dataclasses import dataclass
from typing import Callable


@dataclass
class Calculator:
    operation: Callable[[int, int], int]

    def perform_operation(self):
        return self.operation


def do_addition(a: int, b: int) -> int:
    return a * b


calc = Calculator(do_addition(5, 20))

print(calc.perform_operation())
