# %%
import re

digits = []
trimmed = []

p2 = r"(?:one|two|three|four|five|six|seven|eight|nine|\d+)"

p1_total = 0
p2_total = 0

p2_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open("../data/d01.txt", "r") as f:
    for line in f:
        d1 = "".join(re.findall(r"\d+", line))
        p1_total += int(d1[0] + d1[-1])

        d2 = re.findall(p2, line)
        temp = []
        for d in d2:
            try:
                _ = int(d)
                temp.append(d)
            except:
                temp.append(str(p2_dict[d]))
        temp = "".join(temp)
        print(temp)
        p2_total += int(temp[0] + temp[-1])


print(p1_total, p2_total)
# %%
