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
        # digits = [match.group() for match in re.finditer(pattern, line)]
        # p1_temp = []
        # p2_temp = []
        # for digit in digits:
        #     if digit.isdigit():
        #         p1_temp.append(digit)
        #         p2_temp.append(digit)
        #     else:
        #         p2_temp.append(str(words.index(digit) + 1))
        # p1_digits.append("".join(p1_temp))
        # p2_digits.append("".join(p2_temp))
        p1, p2 = [], []
        for i, d in enumerate(line):
            if d.isdigit():
                p1.append(d)
                p2.append(d)
            else:
                for j, word in enumerate(words):
                    if line[i:].startswith(word):
                        p2.append(str(j + 1))
        p1_digits.append("".join(p1))
        p2_digits.append("".join(p2))


print(sum([int(x[0] + x[-1]) for x in p1_digits]))
print(sum([int(x[0] + x[-1]) for x in p2_digits]))
