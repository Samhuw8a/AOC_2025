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


def construct_valid_ids2(start: int, end: int, repeat: int, block) -> list:
    res: list = []
    bound = max(start, end)
    for i in range(start, end):
        res.append(int(str(i)[:block]*repeat))
    return res


def get_pairs(gap: Gaps) -> list[int]:
    vleft, vright = gap.endpoints
    left = vleft.value
    right = vright.value

    start = split_number(left, False)
    end = split_number(right, True)
    # print(construct_valid_ids(start, end))
    return list(filter(lambda x: left <= x <= right, construct_valid_ids(start, end)))


def get_pairs2(gap: Gaps) -> list[int]:
    vleft, vright = gap.endpoints
    left = vleft.value
    right = vright.value

    min_length = len(str(left))
    max_length = len(str(right))
    result: list = []
    for i in range(1, (min_length//2)+2):
        for j in range(min_length, max_length+2):
            # extend block size i to length min_length+j
            repeat = j//i
            if repeat >= 2:
                # result.append(int(str(i)*repeat))
                # print(i, repeat)
                # print(list(filter(lambda x: left <= x <= right,
                # construct_valid_ids2(start, end, repeat=repeat))))
                # print()
                result.extend(construct_valid_ids2(left, right, repeat, i))

    filtered = filter(lambda x: x in gap, result)
    # print(left,right)
    return list(set(filtered))


def part1() -> None:
    transformed = map(parse_line, input_1)
    result = map(get_pairs, transformed)
    # print(list(result))
    print(f"part1: {sum(map(sum, result))}")


def part2() -> None:
    # print(get_pairs2(Gaps([998, 1012])))
    transformed = map(parse_line, input_1)
    result = map(get_pairs2, transformed)
    # print(list(result))
    print(f"part2: {sum(map(sum,result))}")


def main() -> int:
    part1()
    part2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
