from __future__ import annotations
from itertools import combinations

from utils.all import *
from math import dist

rinput_8 = read_input_line("test_08", sep="\n")
rinput_8 = read_input_line(8, sep="\n")
# print(rinput_8)
input_8 = mapl(lambda x: list(integers(x)), rinput_8)


def distance_between(v: list, u: list) -> float:
    return dist(u, v)


def construct_graph(points: list) -> list:
    q: list = []
    seen: list = []
    for u, v in combinations(points, 2):
        q.append((distance_between(u, v), (u, v)))

    # for i, v in enumerate(points):
    # for j in range(i, len(points)):
    # u = points[j]
    # if u == v or set((i, j)) in seen:
    # continue
    # seen.append(set((i, j)))
    # # heapq.heappush(q, (distance_between(v, u), (u, v)))
    # q.append((distance_between(u,v),(u,v)))
    return q


def part1() -> None:
    lights = input_8.copy()
    UF: UnionFind = UnionFind(mapl(tuple, lights))
    queue = construct_graph(mapl(tuple, lights))
    queue.sort()
    repr: dict = {i: i for i in mapl(tuple, lights)}

    for t in range(1000):
        dist, nodes = queue.pop(0)
        # print(nodes)
        u, v = mapl(tuple, nodes)

        if (repr[u] == repr[v]):
            continue
        UF.merge(u, v)

    distances = []
    for i in UF.components:
        distances.append(len(i))
    distances.sort()

    print(f"part1: {distances[-1]*distances[-2] * distances[-3]}")


def part2() -> None:
    lights = input_8.copy()
    UF: UnionFind = UnionFind(mapl(tuple, lights))
    queue = construct_graph(mapl(tuple, lights))
    queue.sort()
    repr: dict = {i: i for i in mapl(tuple, lights)}

    while len(UF.components) > 1:
        dist, nodes = queue.pop(0)
        u, v = mapl(tuple, nodes)

        if (repr[u] == repr[v]):
            continue
        UF.merge(u, v)
    print(f"part2: {u[0]*v[0]}")


def main() -> int:
    part1()
    part2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
