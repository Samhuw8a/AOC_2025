from __future__ import annotations
from utils.all import *
from collections import defaultdict


rinput_7 = read_input_line("test_07", sep="\n")
rinput_7 = read_input_line(7, sep="\n")
input_7 = mapl(list, rinput_7)
start = rinput_7[0].find("S")


def part1() -> None:
    beam_locations: list = [start]
    count: int = 0
    for row in input_7:
        # print(beam_locations)
        newbeams = beam_locations.copy()
        for idx in range(len(beam_locations)):
            beam = beam_locations[idx]
            if row[beam] == "^":
                count += 1
                newbeams.remove(beam)
                newbeams.append(beam-1)
                newbeams.append(beam+1)

        beam_locations = list(set(newbeams))
    # print(count, beam_locations)
    print(f"part1: {count}")


def part2() -> None:
    beam_locations: list = [start]
    beam_dim: defaultdict = defaultdict(lambda: 0)
    beam_dim[start] = 1
    for row in input_7:
        # print(beam_locations)
        newbeams = beam_locations.copy()
        for idx in range(len(beam_locations)):
            beam = beam_locations[idx]
            if row[beam] == "^":

                prev: int = beam_dim[beam]
                beam_dim[beam-1] += prev
                beam_dim[beam+1] += prev
                beam_dim[beam] =0

                newbeams.remove(beam)
                newbeams.append(beam-1)
                newbeams.append(beam+1)

        beam_locations = list(set(newbeams))
    res = 0
    for k, v in beam_dim.items():
        if k in beam_locations:
            res += v
    print(f"part2: {res}")


def main() -> int:
    part1()
    part2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
