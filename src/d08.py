# %%
from playground import *
import re
from math import lcm

lines = load_input_lines(__file__)

dirs = [0 if c == "L" else 1 for c in lines[0]]

nodes = {}
for line in lines[2:]:
    node, opts = line.split(" = ")
    nodes[node] = re.findall("\w+", opts)

steps = 0

current = "AAA"

while current != "ZZZ":
    steps += 1
    d = dirs[(steps % len(dirs)) - 1]
    current = nodes[current][d]

print("Part 1:", steps)


starts = [x for x in nodes.keys() if x[-1] == "A"]
dests = [x for x in nodes.keys() if x[-1] == "Z"]

path_lengths = []

for s in starts:
    steps = 0
    while s[-1] != "Z":
        steps += 1
        d = dirs[(steps % len(dirs)) - 1]
        s = nodes[s][d]
    path_lengths.append(steps)

print("Part 2:", lcm(*path_lengths))

# %%
