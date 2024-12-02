#!/usr/bin/python3

from enum import Enum
from typing import List


class SafetyClass(Enum):
    UNSAFE = 0
    SAFE = 1


def basic_safety_strategy(levels: List[int]) -> SafetyClass:
    diff_range = (1,3)
    previous_direction = None

    for i in range(1, len(levels)):
        d = levels[i] - levels[i-1]
        current_direction = d / abs(d) if d != 0 else 0
        if not previous_direction:
            previous_direction = current_direction 
        else:
            if current_direction != previous_direction:
                return SafetyClass.UNSAFE
        if not (diff_range[0] <= abs(d) <= diff_range[1]):
            return SafetyClass.UNSAFE

    return SafetyClass.SAFE


def dampened_safety_strategy(levels: List[int]) -> SafetyClass: 
    if not levels:
        return SafetyClass.UNSAFE
    calculated_safety = basic_safety_strategy(levels)
    if calculated_safety == SafetyClass.SAFE:
        return SafetyClass.SAFE
    for holdout in range(len(levels)):
        holdout_safety = basic_safety_strategy([*levels[:holdout], *levels[holdout+1:]])
        if holdout_safety == SafetyClass.SAFE:
            return SafetyClass.SAFE
    return SafetyClass.UNSAFE


def parse_levels(report: str) -> List[int]:
    return [int(x) for x in report.replace("\n","").split(" ")]


def solution_01(filename):
    with open(filename, 'r') as f:
        return list([basic_safety_strategy(parse_levels(report)) for report in f])


def solution_02(filename):
    with open(filename, 'r') as f:
        return list([dampened_safety_strategy(parse_levels(report)) for report in f])


if __name__ == "__main__":
    print(f"Solution 01: {sum(map(lambda x: x.value, solution_01("./input-01.txt")))}")
    print(f"Solution 02: {sum(map(lambda x: x.value, solution_02("./input-02.txt")))}")

