from __future__ import annotations
from utils.all import *

input_1 = read_input_line("test_01", sep="\n")
input_1 = read_input_line(1, sep="\n")
start: int = 50


def format_input(line: str) -> tuple:
    dir: str = line[0]
    num = list(integers(line))[0]

    return dir, num


def part_1(lines: list[tuple]) -> int:
    number = start
    count = 0
    for i in lines:
        dir, am = i
        if dir == "L":
            number -= am
        elif dir == "R":
            number += am
        number = number % 100

        if (number == 0):
            count += 1
    return count


def part_2(lines: list[tuple]) -> int:
    number = start
    count = 0
    for i in lines:
        dir, am = i

        if dir == "L":
            am = -am

        number, zeroes = count_mod(number, am, 100)
        count += zeroes

    return count


def count_mod(number: int, am: int, mod: int) -> tuple:
    """
    return: number, zeroes
    """
    count = 0
    num = number + am

    if number == 0 and sign(am) == -1:
        count -= 1

    while num < 0:
        num += mod
        count += 1

    while num >= mod:
        num -= mod
        count += 1

    if num == 0 and sign(am) == -1:
        count += 1

    # print(num, count)
    return num, count


def main() -> int:
    lines = mapl(format_input, input_1)
    print(f"part 1: {part_1(lines)}")
    print(f"part 2: {part_2(lines)}")
    # print(count_mod(50+1000, 100))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
