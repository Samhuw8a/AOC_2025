from __future__ import annotations
from utils.all import *
from itertools import combinations
from shapely.geometry import Polygon

rinput_9 = read_input("test_09", sep="\n")
rinput_9 = read_input(9, sep="\n")

input_9 = mapl(integers, rinput_9[:-1])


def part1() -> None:
    max_area: int = 0

    for u, v in combinations(input_9, 2):
        area = (abs(u[0]-v[0])+1) * (abs(u[1]-v[1])+1)
        max_area = max(max_area, area)
    print(f"part1: {max_area}")


def part2() -> None:
    poly: Polygon = Polygon(input_9)
    max_area: int = 0

    for u, v in combinations(input_9, 2):
        rectangle = Polygon([u, [v[0], u[1]], v, [u[0], v[1]]])
        if poly.contains(rectangle):
            area = (abs(u[0]-v[0])+1) * (abs(u[1]-v[1])+1)
            max_area = max(max_area, area)
    print(f"part2: {max_area}")


def main() -> int:
    part1()
    part2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
