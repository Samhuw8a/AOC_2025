from __future__ import annotations
from utils.all import *
from itertools import combinations

rinupt_10 = read_input_line("test_10", sep="\n")
rinupt_10 = read_input_line(10, sep="\n")


def parse_line(line: str) -> list:
    lights = line.split()[0].strip("[]")

    buttons = mapl(tuple, map(integers, line.split()[1:-1]))
    joltage = integers(line.split()[-1])
    return [lights, buttons, joltage]


input_10 = mapl(parse_line, rinupt_10)


def press(lights_str: str, button: tuple) -> str:
    lights = list(lights_str)
    for l in button:
        if lights[l] == ".":
            lights[l] = "#"
        else:
            lights[l] = "."
    return "".join(lights)


def get_min_button_presses(line: list) -> int:
    max_presses = len(line[1])+100

    for presses in range(1, max_presses):
        for button_order in combinations(line[1], r=presses):
            lights = "." * len(line[0])
            for button in button_order:
                lights = press(lights, button)  # type: ignore
                if lights == line[0]:
                    # print(f"Minimum button presses: {presses}")
                    return presses
    return -1


def get_min_button_presses2(line: list) -> int:
    max_presses = len(line[1])+100000

    for presses in range(1, max_presses):
        for button_order in combinations(line[1], r=presses):
            counter: list = [0 for _ in range(len(line[2]))]
            for button in button_order:
                for i in button:
                    counter[i] += 1
                if counter == line[2]:
                    # print(f"Minimum button presses: {presses}")
                    return presses
    return -1


def part1() -> None:
    count: int = 0
    for line in input_10:
        res = get_min_button_presses(line)
        count += res
    print(count)


def part2() -> None:
    count: int = 0
    for line in input_10:
        res = get_min_button_presses2(line)
        count += res
    print(count)


def main() -> int:
    part1()
    part2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
