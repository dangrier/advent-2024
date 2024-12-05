#!/usr/bin/python3

from enum import Enum
import re
from typing import Any, Generator, Iterable, Optional


class Command(Enum):
    MUL = "mul"
    DO = "do"
    DONT = "don't"


class Instruction:
    def __init__(self, command: str, a: Optional[int] = None, b: Optional[int] = None) -> None:
        self.command = Command(command)
        self.a = a
        self.b = b
    def result(self) -> int:
        if self.command == Command.MUL:
            assert self.a
            assert self.b
            return self.a * self.b
        return 0
    def __repr__(self) -> str:
        return f"{self.command.value}({self.a},{self.b})"
    def __str__(self) -> str:
        return self.__repr__()


def extract_tokens(line: str):
    pattern = re.compile(r'(' + "|".join([c.value for c in Command]) + r')\((\d+),(\d+)\)', re.DOTALL)
    return re.findall(pattern, line)


def extract_instructions(line: str) -> Generator[Instruction, None, Any]:
    for token in extract_tokens(line):
        if token[0] in [Command.DO.value, Command.DONT.value]:
            yield Instruction(token[0])
        yield Instruction(token[0], int(token[1]), int(token[2]))


def sum_of(instructions: Iterable[Instruction]) -> int:
    total = 0
    for instruction in instructions:
        total += instruction.result()
    return total


def tokens(s: str):
    enabled = True
    for m in re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", s):
        if m == f"{Command.DO.value}()":
            enabled = True
            continue
        elif m == f"{Command.DONT.value}()":
            enabled = False
            continue
        elif enabled:
            yield extract_instructions(m)


def solution_01(filename: str):
    with open(filename, 'r') as f:
        return sum_of(extract_instructions(f.read()))


def solution_02(fn: str):
    with open(fn, 'r') as f:
        return sum_of([y for x in tokens(f.read()) for y in x])


if __name__ == "__main__":
    print(f"Solution 1: {solution_01('input-01.txt')}")
    print(f"Solution 2: {solution_02('input-02.txt')}")

