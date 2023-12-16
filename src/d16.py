# %%
from playground import load_lines, create_grid

RD = {
    "-": {"r": (0, 1, "r"), "l": (0, -1, "l")},
    "|": {"u": (-1, 0, "u"), "d": (1, 0, "d")},
    "\\": {
        "r": (1, 0, "d"),
        "l": (-1, 0, "u"),
        "u": (0, -1, "l"),
        "d": (0, 1, "r"),
    },
    "/": {"r": (-1, 0, "u"), "l": (1, 0, "d"), "u": (0, 1, "r"), "d": (0, -1, "l")},
    ".": {"r": (0, 1, "r"), "l": (0, -1, "l"), "u": (-1, 0, "u"), "d": (1, 0, "d")},
}


def find_energized(beams, grid, rd):
    seen = set()
    while beams:
        c, d = beams.pop()
        s = grid.get(c)
        if not s or (c, d) in seen:
            continue
        seen.add((c, d))
        if s in "\\/.":
            m = rd[s][d]
            nc = (c[0] + m[0], c[1] + m[1])
            beams.append((nc, m[2]))
        elif s in "-|":
            for nd in rd[s].keys():
                m = rd[s][nd]
                nc = (c[0] + m[0], c[1] + m[1])
                beams.append((nc, m[2]))
    return len(set(s[0] for s in seen))


lines = [list(x) for x in load_lines(__file__)]
C = create_grid(lines)

p1 = find_energized([((0, 0), "r")], C, RD)
p2 = 0

# Search from left and right
for i in range(0, len(lines)):
    for j in [0, len(lines[0]) - 1]:
        beams = [((i, j), "r" if j == 0 else "l")]
        p2 = max(p2, find_energized(beams, C, RD))
# Search from top and bottom
for i in [0, len(lines) - 1]:
    for j in range(0, len(lines[0])):
        beams = [((i, j), "d" if i == 0 else "u")]
        p2 = max(p2, find_energized(beams, C, RD))

print("Part 1:", p1, "\nPart 2:", p2)
