# %%
import re
from playground import *

lines = load_input_lines(__file__)


def match_indices(substring, string):
    pattern = re.compile(f"(?<![0-9]){substring}(?![0-9])")
    match = pattern.search(string)
    if match:
        return [int(i) for i in range(match.start(), match.end())]


p1, p2, num_map, symbol_map = 0, 0, {}, {}

for i, line in enumerate(lines):
    num_map[i] = {}
    for match in re.finditer("\d+", line):
        for j in range(match.start(), match.end()):
            num_map[i][j] = match.group()

    symbol_map[i] = {}
    for j, c in enumerate(line):
        if not c.isdigit() and c != ".":
            symbol_map[i][j] = c


for i, line in enumerate(lines):
    # Part 1
    numbers = re.findall("\d+", line)
    for number in numbers:
        indices = match_indices(number, line)
        number_complete = False
        matches = []
        for j in indices:
            options = list(
                set([(i + y, j + x) for y in [-1, 0, 1] for x in [-1, 0, 1]])
            )
            for option in options:
                level_1 = symbol_map.get(option[0])
                if level_1:
                    level_2 = level_1.get(option[1])
                    if level_2:
                        matches.append(level_2)
        if len(matches) > 0:
            p1 += int(number)

    # Part 2
    for j, char in enumerate(line):
        # Identify if it is a gear
        if char == "*":
            matches = []
            # Check all coordinates for number
            for dh in [-1, 0, 1]:
                for dv in [-1, 0, 1]:
                    val = num_map.get(dh + i).get(dv + j)
                    if val:
                        matches.append(int(val))

            matches = list(set(matches))
            if len(matches) == 2:
                p2 += matches[0] * matches[1]

print(f"Part 1: {p1}\nPart 2: {p2}")
