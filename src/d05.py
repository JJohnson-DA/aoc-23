# %%
import re
import time


start = time.time()

with open("../data/d05.txt", "r") as f:
    chunks = f.read().split("\n\n")

seeds_start = [int(x) for x in re.findall("\d+", chunks[0])]

p1 = seeds_start.copy()
# p2 = set()
# for i in range(0, len(seeds_start)):
#     if i % 2 == 0:
#         # p2.append((seeds_start[i], sum(seeds_start[i : i + 2])))
#         [p2.add(seeds_start[i] + x) for x in range(0, seeds_start[i+1])]


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
