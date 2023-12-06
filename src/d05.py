# %%
import re
import time


start = time.time()

with open("../data/d05.txt", "r") as f:
    chunks = f.read().split("\n\n")

seeds_start = [int(x) for x in re.findall("\d+", chunks[0])]

p1 = seeds_start.copy()

for chunk in chunks[1:]:
    num_map = {}
    groups = chunk.split(":\n")[1:][0].split("\n")
    for group in groups:
        destination, source, steps = [int(x) for x in group.split()]
        num_map[(source, destination)] = steps

    # new temp list to add new seed values to
    new_seeds = []

    # For each seed
    for seed in p1:
        seed_match = False
        # for each key, value in num map
        for key, value in num_map.items():
            # check if seed value is between the tuple values
            if key[0] <= seed <= (key[0] + value) and not seed_match:
                seed_val = seed - (key[0] - key[1])
                new_seeds.append(seed_val)
                seed_match = True
        if not seed_match:
            new_seeds.append(seed)

    p1 = new_seeds.copy()

print(f"Part 1: {min(p1)}\nRun Time: {time.time() - start}")

# %%
import re

with open("../data/d05.txt", "r") as f:
    chunks = f.read().split("\n\n")

# * character assigns remaining elements in list to rules as a list
seeds, *rules = chunks
seeds = [int(x) for x in re.findall("\d+", seeds)]


class Rule:
    def __init__(self, rule):
        groups = [line for line in rule.split("\n")[1:]]
        self.rule_ranges = [[int(x) for x in group.split()] for group in groups]

    def apply_rule(self, seed):
        for dest, src, steps in self.rule_ranges:
            # check if seed lies between current range
            if src <= seed <= (src + steps):
                # return new seed value
                return seed - src + dest
        # Return orginal value not in any of the ranges
        return seed


rules = [Rule(r) for r in rules]

p1 = []
for seed in seeds:
    for rule in rules:
        seed = rule.apply_rule(seed)
    p1.append(seed)

print(min(p1))
