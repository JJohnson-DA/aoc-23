# %%
from playground import *

with open("../data/d13.txt", "r") as f:
    maps = [line.split("\n") for line in f.read().split("\n\n")]


class ValleyMap:
    def __init__(self, map) -> None:
        self.map = map

    def transpose(self, l):
        return list(zip(*l))

    def find_horizontal(self, l, part):
        for i in range(1, len(l)):
            top = l[:i][::-1]
            bottom = l[i:]

            top = top[: len(bottom)]
            bottom = bottom[: len(top)]
            if part == 1:
                if top == bottom:
                    return i
            if part == 2:
                if (
                    sum(sum(a != b for a, b in zip(x, y)) for x, y in zip(top, bottom))
                    == 1
                ):
                    return i

        return 0

    def find_vertical(self, l, part):
        l = self.transpose(l)
        sym_max = self.find_horizontal(l, part)
        return sym_max

    def score_map(self, l, part=1):
        h = self.find_horizontal(l, part)
        v = self.find_vertical(l, part)
        if h != 0:
            return h * 100
        else:
            return v


maps = [ValleyMap(m) for m in maps]
print("Part 1:", sum(m.score_map(m.map) for m in maps))
print("Part 2:", sum(m.score_map(m.map, part=2) for m in maps))
