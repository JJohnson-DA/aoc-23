# %%

import re
from playground import *

lines = load_input_lines(__file__)


def contains_symbol(string):
    for char in string:
        if not char.isdigit() and char != ".":
            return True

    return False


def match_indices(substring, string):
    pattern = re.compile(f"(?<![0-9]){substring}(?![0-9])")
    match = pattern.search(string)
    if match:
        return [int(i) for i in range(match.start(), match.end())]


def extract_perimiter(indices, i, lines):
    max_len = len(lines[0]) - 1
    start_c = max(indices[0] - 1, 0)
    end_c = min(indices[-1] + 2, max_len)

    start_r = max(i - 1, 0)
    end_r = min(i + 2, len(lines))

    chars = ""

    for column in range(start_c, end_c):
        for row in range(start_r, end_r):
            chars += lines[row][column]

    return "".join(x if not x.isdigit() else "" for x in chars)


p1 = 0
p2 = 0

num_map = {}

for i, line in enumerate(lines):
    num_map[i] = {}
    for match in re.finditer("\d+", line):
        for j in range(match.start(), match.end()):
            num_map[i][j] = match.group()

for i, line in enumerate(lines):
    # Part 1
    numbers = re.findall("\d+", line)
    for number in numbers:
        indices = match_indices(number, line)
        if indices:
            perimiter = extract_perimiter(indices, i, lines)
            if contains_symbol(perimiter):
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
