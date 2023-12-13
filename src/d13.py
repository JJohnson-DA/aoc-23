# %%
from playground import *

with open("../data/d13.txt", "r") as f:
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
        return sym_max

    def check_bottom(self, l):
        sym_max = 0
        for i in range(0, len(l)):
            # Find symmetry from bottom
            bottom = l[i:]
            top = l[i - len(bottom) : i][::-1]
            if top == bottom:
                sym_max = max(sym_max, i)
        return sym_max

    def find_horizontal(self, l):
        t = self.check_top(l)
        b = self.check_bottom(l)
        return max(t, b)

    def find_vertical(self, l):
        l = self.transpose(l)
        sym_max = self.find_horizontal(l)
        return sym_max

    def score_map(self):
        l = self.map
        h = self.find_horizontal(l)
        v = self.find_vertical(l)
        return v + (100 * h)


sum(ValleyMap(map).score_map() for map in maps)
