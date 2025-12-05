from __future__ import annotations
from utils.all import *
from mind_the_gaps.gaps import Gaps

input_5 = read_input_line("test_05", sep="\n\n")
input_5 = read_input_line(5, sep="\n\n")

gaps = input_5[0].split("\n")
gaps: list[Gaps] = mapl(lambda x: Gaps(mapl(int, x.split("-"))), gaps)  # type:ignore
ids = integers(input_5[1])


def part1() -> None:
    count: int = 0
    for i in ids:
        for g in gaps:
            if i in g:  # type:ignore
                count += 1
                break
    print(f"part 1: {count}")


def count_el(g: Gaps) -> int:
    count = 0
    for i in range(0, len(g.endpoints)-1, 2):
        left = g.endpoints[i].value
        right = g.endpoints[i+1].value
        count += right-left+1
    return count


def part2() -> None:
    G: Gaps = Gaps()
    for g in gaps:
        G = G | g  # type:ignore

    print(f"part 2: {count_el(G)}")


def main() -> int:
    part1()
    part2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
