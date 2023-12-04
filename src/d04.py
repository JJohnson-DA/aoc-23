# %%
from playground import *
import re

lines = load_input_lines(__file__)

cards = {}

for line in lines:
    id, card = line.split(":")
    id = int(re.findall("\d+", id)[0])
    cards[id] = {}
    nums = card.split("|")

    winners = set(re.findall("\d+", nums[0]))
    given = set(re.findall("\d+", nums[1]))
    matches = len(given.intersection(winners))
    score = (2 ** (matches - 1)) if matches > 0 else 0

    cards[id]["score"] = score
    cards[id]["count"] = 1
    cards[id]["num_matches"] = matches
    cards[id]["to_copy"] = [x for x in range(id + 1, id + matches + 1)]

for id, contents in cards.items():
    for i in range(contents["count"]):
        for j in contents["to_copy"]:
            cards[j]["count"] += 1

print(
    f"Part 1: {sum(x['score'] for x in cards.values())}\nPart 2: {sum(x['count'] for x in cards.values())}"
)
