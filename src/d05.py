# %%
# Got stuck and looked at other's code to learn from.
# Largely followed @jonathonpaulson

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

    def part_one(self, seed):
        for dest, src, steps in self.rule_ranges:
            # check if seed lies between current range
            if src <= seed <= (src + steps):
                # return new seed value
                return seed - src + dest
        # Return orginal value not in any of the ranges
        return seed

    def part_two(self, ranges):
        # List to append mapped ranges to
        mapped = []
        # Iterate over rule ranges
        for dest, src, steps in self.rule_ranges:
            src_end = src + steps
            # list to add unmatched ranges
            unmatched = []
            # Iterate while range is not empty
            while ranges:
                # extract a range to iterate over
                range_start, range_end = ranges.pop()

                # Check for unmatched at the start
                start = (range_start, min(range_end, src))
                # If [1] > [0], there was a valid range which didn't match
                if start[1] > start[0]:
                    unmatched.append(start)

                # Check for middle overlap
                middle = (max(range_start, src), min(range_end, src_end))
                # If [1] > [0], the range matched and we must map it and save
                if middle[1] > middle[0]:
                    # Map like we did in part one
                    mapped_start = middle[0] - src + dest
                    mapped_end = middle[1] - src + dest
                    mapped.append((mapped_start, mapped_end))

                # Check for unmatched at the end
                end = (max(range_start, src_end), range_end)
                # If [1] > [0], there was a valid range which didn't match
                if end[1] > end[0]:
                    unmatched.append(end)

            # Reset ranges to unmatched ranges in order to iterate further
            ranges = unmatched

        # Return mapped ranges plus any that didn't map
        return ranges + mapped


# Create Rule class for each set of rules
rules = [Rule(r) for r in rules]

# Part 1
p1 = []
for seed in seeds:
    for rule in rules:
        seed = rule.part_one(seed)
    p1.append(seed)

# get seed ranges for part 2
seed_ranges = []
for i in range(0, len(seeds)):
    if i % 2 == 0:
        seed_ranges.append((seeds[i], sum(seeds[i : i + 2])))

p2 = []
for r in seed_ranges:
    # create list so we can pop and append to in the loop
    ranges = [r]
    for rule in rules:
        # Reassign ranges based on results from previous rules evaluation
        ranges = rule.part_two(ranges)
    # Append the lower bound of the minimum range
    p2.append(min(ranges)[0])

# Print Results
print(f"Part 1: {min(p1)}\nPart 2: {min(p2)}")
