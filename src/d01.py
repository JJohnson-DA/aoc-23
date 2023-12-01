# %%
import re

pattern = r"(?:one|two|three|four|five|six|seven|eight|nine|\d+)"

p1_digits = []
p2_digits = []

words = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

with open("../data/d01.txt", "r") as f:
    for line in f:
        p1 = []
        for i, d in enumerate(line):
            if d.isdigit():
                p1.append(d)
        p1_digits.append("".join(p1))

        p2 = []
        for i, d in enumerate(line):
            if d.isdigit():
                p2.append(d)
            else:
                for j, word in enumerate(words):
                    if line[i:].startswith(word):
                        p2.append(str(j + 1))
        p2_digits.append("".join(p2))


print(sum([int(x[0] + x[-1]) for x in p1_digits]))
print(sum([int(x[0] + x[-1]) for x in p2_digits]))
