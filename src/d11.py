# %%
from playground import *
from itertools import combinations

lines = load_lines(__file__)


class CosmicExpansion:
    def __init__(self, lines):
        self.lines = lines
        self.rows, self.cols = self._find_expanse(self.lines)
        self.galaxies = self._find_galaxies(self.lines, "#")
        self.galaxy_pairs = list(combinations(self.galaxies, 2))

    def _find_expanse(self, lines):
        r = []
        for i in range(len(lines)):
            if all(x == "." for x in lines[i]):
                r.append(i)
        c = []
        for j in range(len(lines[0])):
            js = [lines[i][j] for i in range(len(lines))]
            if all(x == "." for x in js):
                c.append(j)
        return r, c

    def _find_galaxies(self, lines, galaxy_char):
        galaxies = [
            (i, j)
            for i in range(len(lines))
            for j in range(len(lines[0]))
            if lines[i][j] == galaxy_char
        ]
        return galaxies

    def find_steps(self, extra_steps):
        t = 0
        for s, e in self.galaxy_pairs:
            rise = abs(s[0] - e[0])
            run = abs(s[1] - e[1])

            er = len(
                [r for r in self.rows if r > min(s[0], e[0]) and r < max(s[0], e[0])]
            )
            ec = len(
                [c for c in self.cols if c > min(s[1], e[1]) and c < max(s[1], e[1])]
            )

            td = rise + run + er * extra_steps + ec * extra_steps
            t += td
        return t


tool = CosmicExpansion(lines)

print("Part 1:", tool.find_steps(1))
print("Part 2:", tool.find_steps(999999))
