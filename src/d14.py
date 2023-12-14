# %%
from playground import load_lines
from collections import Counter
import time
from copy import deepcopy

lines = [list(x) for x in load_lines(__file__)]

start = time.time()


class Reflector:
    def __init__(self, lines) -> None:
        self.grid = [list(x) for x in lines]

    def rotate_grid(self, g):
        r, c = len(g), len(g[0])
        g = [[g[i][j] for i in range(r - 1, -1, -1)] for j in range(c)]
        return g

    def roll_rocks(self, g):
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
            g[k[0]][k[1]] = v

        return g

    def cycle(self, g):
        # Should end with north facing grid
        for d in ["N", "W", "S", "E"]:
            g = self.rotate_grid(self.roll_rocks(g))
        return g

    def find_loop_length(self, g):
        count = 0
        starts = {}
        while True:
            key = tuple(tuple(x) for x in g)
            if starts.get(key):
                return (starts.get(key), count, g)
            else:
                starts[key] = count
                count += 1
                g = self.cycle(g)

    def score_grid(self, g):
        p1 = 0
        for i, line in enumerate(g[::-1]):
            c = Counter(line)
            p1 += (i + 1) * c["O"]
        return p1

    def part_one(self):
        g = deepcopy(self.grid)
        self.roll_rocks(g)
        print(f"Part 1: {self.score_grid(g)}")

    def part_two(self, iters=1e9):
        g = deepcopy(self.grid)
        start, end, g = self.find_loop_length(g)
        loops_needed = int((iters - start) % (end - start))
        for i in range(loops_needed):
            g = self.cycle(g)
        print(f"Part 2: {self.score_grid(g)}")


R = Reflector(lines)
R.part_one()
R.part_two()
