# %%
from playground import *
import networkx as nx
from itertools import combinations

lines = load_lines("test")
lines = load_lines(__file__)


def find_expanse(lines):
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


def find_galaxies(lines, galaxy_char):
    galaxies = [
        (i, j)
        for i in range(len(lines))
        for j in range(len(lines[0]))
        if lines[i][j] == galaxy_char
    ]
    return galaxies


rows, cols = find_expanse(lines)
g = find_galaxies(lines, "#")
gp = list(combinations(g, 2))

extra_steps = 1

t = 0

for s, e in gp:
    rise = abs(s[0] - e[0])
    run = abs(s[1] - e[1])

    er = len([r for r in rows if r > min(s[0], e[0]) and r < max(s[0], e[0])])
    ec = len([c for c in cols if c > min(s[1], e[1]) and c < max(s[1], e[1])])

    td = rise + run + er * extra_steps + ec * extra_steps
    t += td


# %%
# Row and Column Numbers
rn, cn = len(lines), len(lines[0])


def expand_grid(lines, num):
    lines = [[x for x in line] for line in lines]

    for i in range(len(lines)):
        if all(x == "." for x in lines[i]):
            lines[i] = [str(num)] * len(lines[i])

    replace_cols = []
    for j in range(len(lines[0])):
        js = [lines[i][j] for i in range(len(lines))]
        if all(list(set(js)) == [".", str(num)] for x in js):
            replace_cols.append(j)

    for i in range(len(lines)):
        for j in replace_cols:
            lines[i][j] = str(num)

    return lines


def get_galaxies(grid, galaxy_char):
    galaxies = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[0]))
        if grid[i][j] == galaxy_char
    ]
    return galaxies


def edit_grid(grid):
    final_grid = []
    for i in range(len(grid)):
        row = [int(x.replace("#", "1").replace(".", "1")) for x in grid[i]]
        final_grid.append(row)

    return final_grid


grid = expand_grid(lines, 1000000)
galaxies = get_galaxies(grid, "#")
grid = edit_grid(grid)


# %%
G = nx.Graph()

all_coords = {(i, j): grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))}

for (i, j), c in all_coords.items():
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i + di, j + dj
        nc = all_coords.get((ni, nj))
        if nc:
            G.add_edge(u_of_edge=(i, j), v_of_edge=(ni, nj), weight=c)


pairs = list(combinations(galaxies, 2))

# Initialize the sum of edge weights
sum_of_weights = 0

for g1, g2 in pairs:
    path = nx.dijkstra_path(G, source=g1, target=g2)
    # Iterate over the edges on the shortest path and accumulate the weights
    for i in range(len(path) - 1):
        edge_weight = G[path[i]][path[i + 1]]["weight"]
        sum_of_weights += edge_weight
# G.get_edge_data(u = (0,0), v = (0,1))

# %%

lines = load_lines(__file__)
