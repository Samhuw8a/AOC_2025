from __future__ import annotations
from utils.all import *
from collections import defaultdict

input_4 = read_input_line("test_04", sep="\n")
input_4 = read_input_line(4, sep="\n")

input_4 = mapl(list, input_4)
# print(input_4)


def part1() -> None:
    count: int = 0
    for i in range(len(input_4)):
        for j in range(len(input_4[i])):
            neigh: int = 0
            if input_4[i][j] == "@":
                for n in neighbors8_values(input_4, i, j, ()):
                    if n == "@":
                        neigh += 1
                if neigh < 4:
                    # print(i, j)
                    count += 1

    print(f"part1: {count}")


def count_pass(M) -> tuple:
    count: int = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            neigh: int = 0
            if M[i][j] == "@":
                for n in neighbors8_values(M, i, j, ()):
                    if n == "@":
                        neigh += 1
                if neigh < 4:
                    M[i][j] = "."
                    count += 1

    return count, M


def part2() -> None:
    count: int = 0
    M = input_4
    for i in range(len(input_4)*len(input_4[0])):
        ncount, M = count_pass(M)
        if (ncount == 0):
            break
        count += ncount
    print(f"part2: {count}")
    pass


def main() -> int:
    part1()
    part2()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
