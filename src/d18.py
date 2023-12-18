# %%
from playground import *
from shapely.geometry import Polygon

lines = load_lines("test")
lines = load_lines(__file__)

D = [[x[0], int(x[1]), x[2]] for x in [line.split() for line in lines]]

M = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

for part in [1, 2]:
    start = (0, 0)

    coords = []
    for letter, steps, code in D:
        if part == 2:
            letter = "RDLU"[int(code[-2])]
            steps = int(code[2:-2], 16)
        next = (start[0] + M[letter][0] * steps, start[1] + M[letter][1] * steps)
        coords.append(next)
        start = coords[-1]

    result = get_area(coords)

    print(f"Part {part}: {result}")
