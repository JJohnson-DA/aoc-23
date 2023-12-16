# %%
from playground import load_lines

lines = [list(x) for x in load_lines(__file__)]
C = {(i, j): lines[i][j] for i in range(len(lines)) for j in range(len(lines[0]))}


RD = {
    "-": {
        "r": (0, 1, "r"),
        "l": (0, -1, "l"),
    },
    "|": {
        "u": (-1, 0, "u"),
        "d": (1, 0, "d"),
    },
    "\\": {
        "r": (1, 0, "d"),
        "l": (-1, 0, "u"),
        "u": (0, -1, "l"),
        "d": (0, 1, "r"),
    },
    "/": {
        "r": (-1, 0, "u"),
        "l": (1, 0, "d"),
        "u": (0, 1, "r"),
        "d": (0, -1, "l"),
    },
    ".": {
        "r": (0, 1, "r"),
        "l": (0, -1, "l"),
        "u": (-1, 0, "u"),
        "d": (1, 0, "d"),
    },
}


def find_energized(beams):
    seen = set()
    while beams:
        # Get coord and direction, and symbol for coordinate
        c, d = beams.pop()
        s = C.get(c)
        # if off grid, or already seen this combo, skip remaining step
        if not s or (c, d) in seen:
            continue
        # add combo to seen
        seen.add((c, d))
        # based on symbol, determine next beams and add accordingly
        if s in "\\/.":
            m = RD[s][d]
            nc = (c[0] + m[0], c[1] + m[1])
            beams.append((nc, m[2]))
        elif s in "-|":
            for nd in RD[s].keys():
                m = RD[s][nd]
                nc = (c[0] + m[0], c[1] + m[1])
                beams.append((nc, m[2]))
    return len(set(s[0] for s in seen))


p2 = 0

for i in range(0, len(lines)):
    for j in [0, len(lines[0]) - 1]:
        beams = [((i, j), "r" if j == 0 else "l")]
        p2 = max(p2, find_energized(beams))

for i in [0, len(lines) - 1]:
    for j in range(0, len(lines[0])):
        beams = [((i, j), "d" if i == 0 else "u")]
        p2 = max(p2, find_energized(beams))

print("Part 1:", find_energized([((0, 0), "r")]))
print("Part 2:", p2)
