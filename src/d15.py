# %%
from playground import *

with open("../data/d15.txt", "r") as f:
    lines = f.read().split(",")


def get_hash(code):
    current = 0
    for c in code:
        current = ((current + ord(c)) * 17) % 256

    return current


def split_line(line):
    if "=" in line:
        return line.split("=")
    if "-" in line:
        return line.split("-")


print(f"Part 1: {sum(get_hash(line) for line in lines)}")

boxes = {i: {} for i in range(0, 256)}

for line in lines:
    c, fl = split_line(line)
    bn = get_hash(c)
    if fl == "":
        if boxes[bn].get(c):
            boxes[bn].pop(c)
    else:
        if boxes[bn].get(c):
            boxes[bn][c] = fl
        else:
            boxes[bn][c] = fl

p2 = 0
for b, bl in boxes.items():
    p2 += sum((1 + b) * (i + 1) * int(lv[1]) for i, lv in enumerate(bl.items()))

print("Part 2:", p2)
