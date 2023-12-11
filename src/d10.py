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
# Create Graph Object to add edges to
G = nx.Graph()

# We don't know what pipe 'S' represents..so brute force check each?...
# for p in ["-", "|", "F", "J", "7", "L"]:
for (i, j), sym in all_coords.items():
    # Check if start, replace with correct symbol
    if sym == "S":
        start = (i, j)
        sym = "-"  # hard coded after solving
    # for each direction to check
    for dir in chars[sym]:
        # Get index modifiers for direction
        di, dj = movements[dir]["m"]
        # Create indices for point to check using modifiers
        ni, nj = i + di, j + dj
        # get the symbol if the point exists in the coordinates
        nsym = all_coords.get((ni, nj))
        # If it exists, add an edge from the old to the new point
        if nsym in movements[dir]["valid"]:
            G.add_edge(u_of_edge=(i, j), v_of_edge=(ni, nj))

# Get all cycles (loops) where the cycle contains our start point
target_cycles = [cycle for cycle in nx.simple_cycles(G) if start in cycle]
# There should only be one, divide length by two to get furthest point
if target_cycles:
    print(f"Furthest Point: {len(target_cycles[0]) / 2}")

# Create a polygon from the loop's coordinates
p = Polygon(target_cycles[0])

# Count points within the loop
contained = sum(
    p.contains(Point(i)) for i in all_coords.keys() if i not in target_cycles[0]
)

print("Contained Points:", contained)
