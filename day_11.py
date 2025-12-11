from __future__ import annotations
from utils.all import *
from collections import deque

rinput11 = read_input_line("test_11", sep="\n")
rinput11 = read_input_line(11, sep="\n")

input11 = mapl(lambda x: (x.split(":")[0], x.split(":")[1].split()), rinput11)

G: dict = dict()
for name, connections in input11:
    G[name] = connections

G["out"] = []


def part1() -> None:
    queue: deque = deque([("you", set())])
    count: int = 0

    while queue:
        current, visited = queue.popleft()

        if (current == "out"):
            # print(visited)
            count += 1
            continue

        visited.add(current)
        for neighbor in G[current]:
            if neighbor not in visited:
                queue.append((neighbor, visited))

    print(count)


def count_paths(start: str, target: str) -> int:
    queue: deque = deque([(start, list())])
    count: int = 0

    while queue:
        current, visited = queue.popleft()

        if (current in visited):
            continue

        visited = visited.copy()
        visited.append(current)

        if (current == target):
            count += 1
            continue

        for neighbor in G[current]:
            queue.append((neighbor, visited))

    return count


def part2() -> None:
    total_paths: int = 0
    total_paths += (
    count_paths("svr", "fft") *
    count_paths("fft", "dac") *
    count_paths("dac", "out")
    )
    # total_paths: int = count_paths("dac", "fft")
    print(total_paths)


def main() -> int:
    part1()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
