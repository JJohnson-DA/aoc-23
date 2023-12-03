# %%
from playground import *
import re

# get input file
games = load_input_lines(__file__)

# Lists to append to
possible_total = 0
powers = 0

for game in games:
    id, logs = game.split(":")
    id = int(re.findall("\d+", id)[0])
    logs = [x.strip() for x in logs.split(";")]

    results = []
    power = {}

    for log in logs:
        pulls = log.split(", ")
        for pull in pulls:
            num, color = pull.split(" ")
            num = int(num)
            if color not in power:
                power[color] = num
            else:
                power[color] = max(power[color], num)

            if (
                (color == "blue" and num > 14)
                or (color == "red" and num > 12)
                or (color == "green" and num > 13)
            ):
                results.append(True)
            else:
                results.append(False)
    powers += power["red"] * power["blue"] * power["green"]

    if sum(results) == 0:
        possible_total += id

print(f"Part 1: {possible_total}\nPart 2: {powers}")
