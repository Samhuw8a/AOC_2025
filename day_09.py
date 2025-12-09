from __future__ import annotations
from utils.all import *
from itertools import combinations
from more_itertools import windowed
from mind_the_gaps.gaps import Gaps, Endpoint
from dataclasses import dataclass

rinput_9 = read_input("test_09", sep="\n")
# rinput_9 = read_input(9, sep="\n")

input_9 = mapl(integers, rinput_9[:-1])


@dataclass
class Point():
    coords: list
    type: str

    def __init__(self, coords: list, type: str) -> None:
        self.coords = coords
        self.type = type


def part1() -> None:
    max_area: int = 0

    for u, v in combinations(input_9, 2):
        area = (abs(u[0]-v[0])+1) * (abs(u[1]-v[1])+1)
        max_area = max(max_area, area)
    print(f"part1: {max_area}")


def classify(p: list, edges: tuple) -> Point:
    l, r = edges
    dl = direction((p, l))
    dr = direction((p, r))

    if dl == "u" and dr == "l":
        return Point(coords=p, type="dr")

    if dl == "u" and dr == "r":
        return Point(coords=p, type="dl")

    if dr == "u" and dl == "l":
        return Point(coords=p, type="dr")

    if dr == "u" and dl == "r":
        return Point(coords=p, type="dl")

    if (dr == "d" and dl == "l"):
        return Point(coords=p, type="tr")
    if (dr == "d" and dl == "r"):
        return Point(coords=p, type="tl")
    if (dl == "d" and dr == "l"):
        return Point(coords=p, type="tr")
    if (dl == "d" and dr == "r"):
        return Point(coords=p, type="tl")

    raise Exception("Fuck you")


def direction(edge: tuple):
    p, o = edge
    if o[0] > p[0]:
        return "l"
    if o[0] < p[0]:
        return "r"

    if o[1] > p[1]:
        return "d"
    if o[1] < p[1]:
        return "u"


def valid(u: tuple, v: tuple, greens: dict) -> bool:
    if (
        (u[0] <= v[0] and u[1] < v[1] and greens[u].type == "tl") or
        (u[0] <= v[0] and u[1] < v[1] and greens[v].type == "dr") or
        (v[0] <= u[0] and v[1] < u[1] and greens[v].type == "tl") or
        (v[0] <= u[0] and v[1] < u[1] and greens[u].type == "dr") or

        (u[0] >= v[0] and u[1] > v[1] and greens[u].type == "tr") or
        (u[0] >= v[0] and u[1] > v[1] and greens[v].type == "dl") or
        (v[0] >= u[0] and v[1] > u[1] and greens[v].type == "tr") or
        (v[0] >= u[0] and v[1] > u[1] and greens[u].type == "dl")
    ):
        return True

    return False


def part2() -> None:
    global input_9
    max_area: int = 1

    greens: dict = dict()
    input_9 = mapl(tuple, input_9)

    for i in range(1, len(input_9)-1):
        p = input_9[i]
        l = input_9[i-1]
        r = input_9[i+1]
        greens[p] = classify(p, (l, r))
    greens[input_9[0]] = classify(input_9[0], (input_9[-1], input_9[1]))
    greens[input_9[-1]] = classify(input_9[-1], (input_9[-2], input_9[0]))

    # print(greens)

    for u, v in combinations(input_9, 2):
        if valid(u, v, greens):
            area = (abs(u[0]-v[0])+1) * (abs(u[1]-v[1])+1)
            max_area = max(max_area, area)
    print(f"part2: {max_area}")


def main() -> int:
    part1()
    part2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
