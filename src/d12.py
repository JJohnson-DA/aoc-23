# %%
from playground import *

lines = load_lines("test")


class HotSpring:
    def __init__(self, line) -> None:
        self.map = line.split(" ")[0]
        self.groups = [int(x) for x in line.split(" ")[1].split(",")]


for line in lines:
    spring = HotSpring(line)
    print(spring.groups, spring.map)
