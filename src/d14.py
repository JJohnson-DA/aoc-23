# %%
from playground import load_lines
from collections import Counter
from functools import cache

lines = load_lines("test")
# lines = load_lines(__file__)
lines = [list(x) for x in lines]


class Reflector:
    def __init__(self, lines) -> None:
        self.grid = [list(x) for x in lines]
        self.roll_cache = {}

    # @cache
    def rotate_grid(self):
        r, c = len(self.grid), len(self.grid[0])
        g = [[self.grid[i][j] for i in range(r - 1, -1, -1)] for j in range(c)]
        return g

    # @cache
    def roll_rocks(self, g):
        gt = tuple(tuple(gc) for gc in g)
        if self.roll_cache.get(gt):
            return self.roll_cache.get(gt)
        else:
            gn = g.copy()
            coords = {(i, j): g[i][j] for i in range(len(g)) for j in range(len(g[0]))}
            rocks_rolled = 1
            while rocks_rolled > 0:
                rocks_rolled = 0
                for k, v in coords.items():
                    if v == "O":
                        nv = coords.get((k[0] - 1, k[1]))
                        if nv == ".":
                            coords[((k[0] - 1, k[1]))] = "O"
                            coords[((k[0], k[1]))] = "."
                            rocks_rolled += 1

            for k, v in coords.items():
                gn[k[0]][k[1]] = v

            self.roll_cache[gt] = gn

            return gn

    def cycle(self):
        for i in range(4):
            self.roll_rocks(self.grid)
            self.rotate_grid()

    def score_grid(self):
        p1 = 0
        for i, line in enumerate(self.grid[::-1]):
            c = Counter(line)
            p1 += (i + 1) * c["O"]
        return p1

    def part_one(self):
        self.roll_rocks(self.grid)
        print(f"Part 1: {self.score_grid()}")

    def part_two(self):
        cycles_target = 1000000000
        cycles_run = 0
        while cycles_run < cycles_target:
            cycles_run += 1
            self.cycle()

        print(f"Part 2: {self.score_grid()}")


R = Reflector(lines)
R.part_one()
