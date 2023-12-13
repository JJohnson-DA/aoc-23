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

    def score_map(self, l):
        h = self.find_horizontal(l)
        v = self.find_vertical(l)
        d = "h" if h > 0 else "v"
        return (d, v + (100 * h))

    def swap_char(self, char):
        if char == ".":
            return "#"
        if char == "#":
            return "."

    # def find_smudge(self, l):
    #     sol1 = self.score_map(l)
    #     print(sol1)

    #     for i in range(len(l)):
    #         for j in range(len(l[0])):
    #             l2 = [list(x) for x in l]
    #             l2[i][j] = self.swap_char(l2[i][j])
    #             l2 = ["".join(x) for x in l2]

    #             h = self.find_horizontal(l2)
    #             v = self.find_vertical(l2)

    #             if sol2[1] > 0 and sol2[0] != sol1[0]:
    #                 print("-" * 20)
    #                 return sol2

    #     return sol1


vm = ValleyMap(maps[1])

maps = [ValleyMap(m) for m in maps]
print("Part 1:", sum(m.score_map(m.map)[1] for m in maps))
# print("Part 2:", sum(m.find_smudge(m.map)[1] for m in maps))

# 29807 too high
# 718 too low
# %%
