# %%
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


boxes = {i: {} for i in range(0, 256)}

for line in lines:
    c, fl = split_line(line)
    bn = get_hash(c)
    if fl == "":
        boxes[bn].pop(c, None)
    else:
        boxes[bn][c] = fl

p2 = sum(
    (1 + b) * (i + 1) * int(lv[1])
    for b, bl in boxes.items()
    for i, lv in enumerate(bl.items())
)

print("Part 1:", sum(get_hash(line) for line in lines))
print("Part 2:", p2)
