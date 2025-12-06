from __future__ import annotations
from utils.all import *
from itertools import zip_longest

rinput_6 = read_input_line("test_06", sep="\n")
rinput_6 = read_input_line(6, sep="\n")


input_6 = mapl(lambda x: x.split(), rinput_6)
input_6 = transpose(input_6)  # type:ignore



def parse_lines(lines: list) -> list:
    collms: list = []
    for i, c in enumerate(lines[-1]):
        if (c != " "):
            collms.append(i)

    collms.append(len(lines[-1])+3)

    nlines: list = []
    for idx, line in enumerate(lines):
        nlines.append([])
        for i in range(len(collms)-1):
            nlines[idx].append(line[collms[i]:collms[i+1]-1])
    return nlines


input2_6: list = parse_lines(rinput_6)  # type:ignore
input2_6 = transpose(input2_6)  # type:ignore


def parse_collm(line: list) -> int:
    operator: str = line[-1]
    line = line[:-1]
    calc: str = ""
    for i in line:
        calc += i
        calc += operator
    return eval(calc[:-1])


def parse_collm2(line: list) -> int:
    operator: str = line[-1].strip()
    line = mapl(lambda x: x[::-1],line[:-1])
    calc: str = ""
    for i in zip_longest(*line):
        val = int("".join(i))
        calc += str(val)
        calc += operator
    return eval(calc[:-1])


def part1() -> None:
    print(f"part1: {sum(map(parse_collm, input_6))}")  # type:ignore


def part2() -> None:
    print(f"part2: {sum(map(parse_collm2, input2_6))}")  # type:ignore


def main() -> int:
    part1()
    part2()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
