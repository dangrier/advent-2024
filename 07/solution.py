#!/usr/bin/python3


from enum import Enum
from itertools import product
from typing import List, Literal, Union


class Operator(Enum):
    ADD = "+"
    MUL = "*"
    CONCAT = "|"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def operators_for(solution: Union[Literal[1], Literal[2]]):
        if solution == 1:
            return [Operator.ADD, Operator.MUL]
        if solution == 2:
            return [Operator.ADD, Operator.MUL, Operator.CONCAT]

    def apply(self, a: int, b: int) -> int:
        if self == Operator.ADD:
            return a + b
        if self == Operator.MUL:
            return a * b
        if self == Operator.CONCAT:
            return int(str(a) + str(b))
        return 0


class Line:
    total: int
    components: List[int]

    def __init__(self, text: str):
        self._extract_components(text)

    def _extract_components(self, text: str):
        text_parts = text.split(":")
        self.total = int(text_parts[0])
        self.components = [int(c) for c in text_parts[1].lstrip().split(" ")]

    def _generate_pairs(self):
        return zip(self.components, self.components[1:])

    def _generate_operators(
        self, count: int, solution_mode: Union[Literal[1], Literal[2]]
    ):
        return product(Operator.operators_for(solution_mode), repeat=count)

    def valid_equations(self, solution_mode: Union[Literal[1], Literal[2]]):
        for operator_set in self._generate_operators(
            len(self.components) - 1, solution_mode
        ):
            current_value = self.components[0]
            for op, next_value in zip(operator_set, self.components[1:]):
                current_value = op.apply(current_value, next_value)
            if current_value == self.total:
                yield current_value

    def valid_sum(self, solution_mode: Union[Literal[1], Literal[2]] = 1):
        return sum(self.valid_equations(solution_mode))

    def __str__(self) -> str:
        return f"<Line total={self.total} components={self.components}>"

    def __repr__(self) -> str:
        return self.__str__()


def solution_01():
    with open("./input-01.txt", "r") as f:
        processed_lines = [Line(line) for line in f.readlines()]
        valid_total = sum(
            [
                line.total
                for line in processed_lines
                if line.valid_sum(solution_mode=1) > 0
            ]
        )
        return valid_total


def solution_02():
    with open("./input-02.txt", "r") as f:
        processed_lines = [Line(line) for line in f.readlines()]
        valid_total = sum(
            [
                line.total
                for line in processed_lines
                if line.valid_sum(solution_mode=2) > 0
            ]
        )
        return valid_total


if __name__ == "__main__":
    print(f"Solution 1: {solution_01()}")
    print(f"Solution 2: {solution_02()}")
