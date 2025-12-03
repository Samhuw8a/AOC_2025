from __future__ import annotations
from utils.all import *

input_3 = read_input_line("test_03", sep="\n")
input_3 = read_input_line(3, sep="\n")


def get_biggest_num(line: str) -> int:
    biggest: int = -1
    indx_biggest: int = -1
    sec_biggest: int = -1

    next_biggest: int = -1

    for i in range(len(line)):
        d = int(line[i])
        if d > biggest:
            sec_biggest = biggest
            biggest = d
            indx_biggest = i

    if (indx_biggest == len(line)-1):
        return sec_biggest*10+biggest

    for i in range(indx_biggest+1, len(line)):
        d = int(line[i])
        if d > next_biggest:
            next_biggest = d

    # print(biggest, indx_biggest, next_biggest)
    return biggest*10+next_biggest


def get_nth_biggest(line: str, n: int, start: int) -> tuple:
    max: int = -1
    index: int = -1
    for i in range(start, len(line)-11+n):
        d = int(line[i])
        if d > max:
            max = d
            index = i
    return max, index


def get_biggest_12(line: str) -> int:
    num: int = 0
    index: int = 0

    num, index = get_nth_biggest(line, 0, index)
    for i in range(1, 12):
        digit, index = get_nth_biggest(line, i, index+1)
        num = num*10+digit
    return num


def part1() -> None:
    processed = map(get_biggest_num, input_3)
    # print(list(processed))
    print(f" part1: {sum(processed)}")


def part2() -> None:
    processed = map(get_biggest_12, input_3)
    # print(list(processed))
    print(f" part2: {sum(processed)}")


def main() -> int:
    part1()
    part2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
