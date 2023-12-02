# %%
from playground import *

p1_total, p2_total = 0, 0

words = {number_to_words(num): num for num in range(1, 10)}

with open("../data/d01.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    p1, p2 = [], []
    for i, d in enumerate(line):
        if d.isdigit():
            p1.append(d)
            p2.append(d)
        else:
            for word, num in words.items():
                if line[i:].startswith(word):
                    p2.append(str(num))
    p1_total += int(p1[0] + p1[-1])
    p2_total += int(p2[0] + p2[-1])

print(f"Part 1: {p1_total}\nPart 2: {p2_total}")
