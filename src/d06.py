# %%
from playground import *
import re

t, d = load_input_lines(__file__)
t1 = [int(x) for x in re.findall("\d+", t)]
d1 = [int(x) for x in re.findall("\d+", d)]

t2 = [int("".join([str(x) for x in t1]))]
d2 = [int("".join([str(x) for x in d1]))]


def find_charges(t, d):
    total_charges = 1
    for ti, di in zip(t, d):
        total_charges *= sum(tc * (ti - tc) > di for tc in range(ti))
    return total_charges


print(f"Part 1: {find_charges(t1, d1)}\nPart 2: {find_charges(t2, d2)}")


# %%
