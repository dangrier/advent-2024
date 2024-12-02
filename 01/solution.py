#!/usr/bin/python3


def parse_sorted_lists(filename: str):
    with open(filename, 'r') as f:
        return zip(*[sorted(y) for y in zip(*[x.replace('\n','').split("   ") for x in f.readlines()])])


def solution_01(filename: str):
    return sum(list([abs(int(vals[0])-int(vals[1])) for vals in parse_sorted_lists(filename)]))


def solution_02(filename: str):
    # Collect counts of each digit in each column
    left_counts = {}
    right_counts = {}
    for left, right in parse_sorted_lists(filename):
        left, right = int(left), int(right)
        left_counts[left] = int(left_counts.get(left, 0)) + 1
        right_counts[right] = int(right_counts.get(right, 0)) + 1

    # Add up running total of similarity score
    sim = 0
    for left_k, left_v in left_counts.items():
        right_v = right_counts.get(left_k, 0) # No point worrying about missing left keys as they'd be *0
        sim += left_k * left_v * right_v

    return sim


if __name__ == "__main__":
    print(f'Solution 1: {solution_01('./input-01.txt')}')
    print(f'Solution 2: {solution_02('./input-02.txt')}')

