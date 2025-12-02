from __future__ import annotations
from utils.all import *
from mind_the_gaps.gaps import Gaps, Endpoint
import math

input_1 = read_input_line("test_02", sep=",")
input_1 = read_input_line(2, sep=",")


def parse_line(line: str) -> Gaps:
    left, right = line.split("-")
    g: Gaps = Gaps([int(left), int(right)])
    return g


def split_number(n: int, extend: bool) -> int:
    lenght = len(str(n))
    if extend:
        mid = math.ceil(lenght/2)
    else:
        mid = math.floor(lenght/2)

    if mid == 0:
        mid = 1

    new = int(str(n)[:mid])
    return new


def construct_valid_ids(start: int, end: int) -> list:
    res: list = []
    for i in range(start, end+1):
        res.append(int(str(i)*2))
    return res


def get_pairs(gap: Gaps) -> list[int]:
    vleft, vright = gap.endpoints
    left = vleft.value
    right = vright.value

    try:
        start = split_number(left, False)
        end = split_number(right, True)
    except ValueError as e:
        print(repr(left))
        print(repr(right))
        raise e
    # print(construct_valid_ids(start, end))
    return list(filter(lambda x: left <= x <= right, construct_valid_ids(start, end)))


def main() -> int:
    transformed = map(parse_line, input_1)
    result = map(get_pairs, transformed)
    # print(list(result))
    print(f"part1: {sum(map(sum, result))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
