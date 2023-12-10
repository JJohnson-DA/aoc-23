# %%
from playground import *
import networkx as nx
from shapely.geometry import Polygon, Point


lines = load_lines(__file__)

all_coords = {
    (i, j): lines[i][j] for i in range(len(lines)) for j in range(len(lines[0]))
}

movements = {
    "top": {"valid": ["|", "7", "F"], "m": (-1, 0)},
    "bottom": {"valid": ["L", "J", "|"], "m": (1, 0)},
    "left": {"valid": ["-", "L", "F"], "m": (0, -1)},
    "right": {"valid": ["J", "-", "7"], "m": (0, 1)},
}

# what symbols connect to eachother
chars = {
    "|": ["top", "bottom"],
    "-": ["left", "right"],
    "L": ["top", "right"],
    "J": ["top", "left"],
    "7": ["bottom", "left"],
    "F": ["bottom", "right"],
    ".": [],
    "S": [],
}
G = nx.Graph()

# We don't know what pipe 'S' represents..so brute force check each?...
# for p in ["-", "|", "F", "J", "7", "L"]:
for (i, j), sym in all_coords.items():
    if sym == "S":
        start = (i, j)
        sym = "-"  # hard coded after solving
    for dir in chars[sym]:
        di, dj = movements[dir]["m"]
        ni, nj = i + di, j + dj
        nsym = all_coords.get((ni, nj))

        if nsym in movements[dir]["valid"]:
            G.add_edge(u_of_edge=(i, j), v_of_edge=(ni, nj))

target_cycles = [cycle for cycle in nx.simple_cycles(G) if start in cycle]

if target_cycles:
    print(f"Furthest Point: {len(target_cycles[0]) / 2}")

# Create a polygon from the loop coordinates
loop_polygon = Polygon(target_cycles[0])

# Count points within the loop
points_within_loop = sum(
    loop_polygon.contains(Point(i, j))
    for i in range(len(lines))
    for j in range(len(lines[0]))
    if (i, j) not in target_cycles[0]
)

print("Contained Points:", points_within_loop)
