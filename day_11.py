from __future__ import annotations
from utils.all import *
from collections import deque, defaultdict

rinput11 = read_input_line("test_11", sep="\n")
rinput11 = read_input_line(11, sep="\n")

input11 = mapl(lambda x: (x.split(":")[0], x.split(":")[1].split()), rinput11)

G: dict = dict()
for name, connections in input11:
    G[name] = connections

G["out"] = []


def count_paths(start: str, target: str) -> int:

    # topological order (Kahn's algorithm)
    indeg: defaultdict = defaultdict(int)
    for u in G:
        for v in G[u]:
            indeg[v] += 1

    q = deque([n for n in G if indeg[n] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in G[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    paths_to: defaultdict = defaultdict(lambda: 0)
    # paths_to: defaultdict = defaultdict(int)
    paths_to[start] = 1
    visited: set = set()
    for u in topo:
        for v in G[u]:
            paths_to[v] += paths_to[u]

    return paths_to[target]


def part1() -> None:
    print(f"part1: {count_paths("you", "out")}")


def part2() -> None:
    total_paths: int = 0
    total_paths += (
        count_paths("svr", "fft") *
        count_paths("fft", "dac") *
        count_paths("dac", "out")
    )

    print(f"part2: {total_paths}")


def main() -> int:
    part1()
    part2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
