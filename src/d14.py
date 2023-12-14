# %%
from playground import load_lines
from collections import Counter
from functools import cache

lines = load_lines("test")
lines = load_lines(__file__)
lines = [list(x) for x in lines]


all_coords = {
    (i, j): lines[i][j] for i in range(len(lines)) for j in range(len(lines[0]))
}

ds = [(-1, 0), (0, -1), (1, 0), (0, 1)]

grid_cache = {}

# for i in range(1000000000):
# for d in ds:
#     grid_start = tuple([tuple(x) for x in lines.copy()])

#     if (d, grid_start) in grid_cache.keys():
#         lines = grid_cache[(d, grid_start)]
# else:
for d in ds:
    rocks_rolled = 1
    while rocks_rolled > 0:
        # Reset for look
        rocks_rolled = 0
        for k, v in all_coords.items():
            if v == "O":
                # check item above it, and get coords. if it is empty, roll rock up
                nv = all_coords.get((k[0] + d[0], k[1] + d[1]))
                if nv == ".":
                    all_coords[((k[0] + d[0], k[1] + d[1]))] = "O"
                    all_coords[((k[0], k[1]))] = "."
                    # add to roll count
                    rocks_rolled += 1

    for k, v in all_coords.items():
        lines[k[0]][k[1]] = v

    break

    # grid_cache[(d, grid_start)] = lines

p1 = 0
for i, line in enumerate(lines[::-1]):
    c = Counter(line)
    p1 += (i + 1) * c["O"]
