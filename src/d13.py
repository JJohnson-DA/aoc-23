# %%
from playground import *

with open("../data/test.txt", "r") as f:
    maps = [line.split("\n") for line in f.read().split("\n\n")]


class ValleyMap:
    def __init__(self, map) -> None:
        self.map = map

    def transpose(self, l):
        return ["".join(row) for row in zip(*l)]

    def check_top(self, l):
        sym_max = 0
        for i in range(0, len(l)):
            # Find symmetry from top
            top = l[:i][::-1]
            bottom = l[i : len(top) + i]
            if top == bottom:
                sym_max = max(sym_max, i)
        return (sym_max, l[: sym_max * 2])

    def check_bottom(self, l):
        sym_max = 0
        for i in range(0, len(l)):
            # Find symmetry from bottom
            bottom = l[i:]
            top = l[i - len(bottom) : i][::-1]
            if top == bottom:
                sym_max = max(sym_max, i)
        return (sym_max, l[sym_max * 2 - 1 :])

    def find_horizontal(self, l):
        t = self.check_top(l)
        b = self.check_bottom(l)
        if t[0] > b[0]:
            return t
        else:
            return b

    def find_vertical(self, l):
        l = self.transpose(l)
        sym_max = self.find_horizontal(l)
        return sym_max

    def score_map(self, l):
        h = self.find_horizontal(l)
        v = self.find_vertical(l)
        if h[0] != 0:
            return (h[0] * 100, h[1])
        else:
            return v

    def swap_char(self, char):
        if char == ".":
            return "#"
        if char == "#":
            return "."


vm = ValleyMap(maps[0])

maps = [ValleyMap(m) for m in maps]
print("Part 1:", sum(m.score_map(m.map)[0] for m in maps))
# print("Part 2:", sum(m.find_smudge(m.map)[0] for m in maps))

# 29807 too high
# 718 too low
