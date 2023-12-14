# %%
from playground import *
from functools import cache

lines = load_lines(__file__)


class HotSpring:
    def __init__(self, line) -> None:
        # Part 1 items
        self.map = line.split(" ")[0]
        self.groups = [int(x) for x in line.split(" ")[1].split(",")]
        # Part 2 items
        self.map2 = "?".join([self.map] * 5)
        self.groups2 = self.groups * 5
        # Run part 1
        self.part1 = self.find_combinations(self.map, tuple(self.groups))
        # Run part 2
        self.part2 = self.find_combinations(self.map2, tuple(self.groups2))

    @cache
    def find_combinations(self, map, groups):
        # ---- Base cases to stop recursion ------------------------------------
        # map and groups both empty is valid
        if len(map) == 0 and len(groups) == 0:
            return 1
        # unmatched groups is invalid combination
        if len(map) == 0 and len(groups) != 0:
            return 0
        # No groups and known springs left is invalid
        if len(groups) == 0 and "#" in map:
            return 0

        # initialize counter
        count = 0

        # ---- first character could be a '.' (? or .) -------------------------
        # This effectively delays the match. Had to put this loop first otherwise
        # we get an index error, not sure why at this point.
        if map[0] in ".?":
            # doesn't match, so cut off the first step of map and keep group unchanged
            count += self.find_combinations(map[1:], groups)

        # ---- first character could be a '?' ( # or ?) ------------------------
        # This effectively matches as soon as possible
        # check if we can match the next length in the group
        if (
            len(groups) > 0
            and map[0] in "?#"  # first character is '#' or '?'
            and len(map) >= groups[0]  # next length fits in the remaining map
            and "." not in map[: groups[0]]  # no periods in group length
            and (
                groups[0] == len(map) or map[groups[0]] != "#"
            )  # char after group length is not a '#'
        ):
            # Strip the match and run the function on the remaining pieces
            map = map[
                groups[0] + 1 :
            ]  # add one since we know from above that the next character isn't a '#'
            groups = groups[1:]

            count += self.find_combinations(map, groups)
        # Add map and group set to cache
        return count


p1 = sum(m.part1 for m in [HotSpring(line) for line in lines])
print(f"Part 1: {p1}")

p2 = sum(m.part2 for m in [HotSpring(line) for line in lines])
print(f"Part 2: {p2}")
