from __future__ import annotations
from typing import Final, Literal, NamedTuple, Self, overload
from collections.abc import Iterable, Iterator, ValuesView
from itertools import combinations

from utils.all import *
# from utils.vector import *
from collections import Counter
from collections import defaultdict
import heapq
from math import dist


class UnionFind[T]:
    """A collection for fast unions of disjoint sets."""

    def __init__(self, iterable: Iterable[T] | None = None):
        self._parents: dict[T, T] = {}
        self._ranks: dict[T, int] = {}
        self._components: dict[T, set[T]] = {}

        if iterable is not None:
            for item in iterable:
                self.add(item)

    @property
    def components(self) -> ValuesView[set[T]]:
        """Return the disjoint sets."""
        return self._components.values()

    @property
    def size(self) -> int:
        """Number of items in all disjoint sets."""
        return len(self._parents)

    def __contains__(self, item: T) -> bool:
        return item in self._parents

    def __len__(self) -> int:
        return len(self._components)

    def __getitem__(self, item: T) -> set[T]:
        if item not in self:
            raise KeyError(item)

        root = self.find(item)
        return self._components[root]

    def __iter__(self) -> Iterator[set[T]]:
        """Yield each disjoint set."""
        yield from self._components.values()

    def elements(self) -> Iterator[T]:
        """Yield each element of each disjoint set."""
        yield from self._parents.keys()

    def add(self, item: T) -> None:
        """Add a new item to the disjoint set forest."""
        if item in self:
            return
        self._parents[item] = item
        self._ranks[item] = 0
        self._components[item] = {item}

    def find(self, item: T) -> T:
        """Find the representive of the item's disjoint set."""
        if item not in self:
            raise KeyError(item)

        if self._parents[item] != item:
            self._parents[item] = self.find(self._parents[item])
        return self._parents[item]

    def merge(self, a: T, b: T) -> None:
        """Merge the set containing ``a`` and the set containing ``b``."""
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root:
            return

        if self._ranks[a_root] < self._ranks[b_root]:
            self._parents[a_root] = b_root
            self._components[b_root] |= self._components.pop(a_root)
        elif self._ranks[a_root] > self._ranks[b_root]:
            self._parents[b_root] = a_root
            self._components[a_root] |= self._components.pop(b_root)
        else:
            self._parents[a_root] = b_root
            self._ranks[b_root] += 1
            self._components[b_root] |= self._components.pop(a_root)


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

    print(distances[-1]*distances[-2] * distances[-3])


def part2() -> None:
    lights = input_8.copy()
    UF: UnionFind = UnionFind(mapl(tuple, lights))
    queue = construct_graph(mapl(tuple, lights))
    queue.sort()
    repr: dict = {i: i for i in mapl(tuple, lights)}

    while len(UF.components) > 1:
        dist, nodes= queue.pop(0)
        u, v= mapl(tuple, nodes)

        if (repr[u] == repr[v]):
            continue
        UF.merge(u, v)
    print(u[0]*v[0])


def main() -> int:
    part1()
    part2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
