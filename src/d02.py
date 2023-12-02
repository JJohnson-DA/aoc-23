# %%
from playground import *
import re

# 12 red cubes, 13 green cubes, and 14 blue cubes

game_ids = []
powers = []

# separate into games
with open("../data/d02.txt", "r") as f:
    games = f.readlines()

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

            if (color == "blue") & (num > 14):
                results.append(True)
            elif (color == "red") & (num > 12):
                results.append(True)
            elif (color == "green") & (num > 13):
                results.append(True)
            else:
                results.append(False)
    powers.append(power["red"] * power["blue"] * power["green"])

    if sum(results) == 0:
        game_ids.append(id)


print(f"Part 1: {sum(game_ids)}\nPart 2: {sum(powers)}")
