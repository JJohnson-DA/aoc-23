# %%
from playground import *
import heapq

lines = load_lines(__file__)

grid = create_grid(lines)

dirs = {"r": (0, 1, "l"), "l": (0, -1, "r"), "u": (-1, 0, "d"), "d": (1, 0, "u")}


def get_neighbors(p, m, s, part=1):
    nbs = []
    for k, v in dirs.items():
        valid = False
        # ---- Part 2 ----
        if part == 2:
            # under four steps must be moving same direction
            if s < 4 and m != k:
                continue
            # 4 -> 9 steps, can't move reverse step
            if 4 <= s <= 9 and v[2] == m:
                continue
            # if 10 steps or more and direction is the same
            if s >= 10 and m == k:
                continue
            # if the point passed above, it's valid so we append
            valid = True
        # ---- Part 1
        else:
            # already 3 steps and option is same direction
            if s == 3 and m == k:
                continue
            # option is the reverse of the current direction
            if v[2] == m:
                continue
            valid = True
        if valid:
            # If passed above, it's valid so we append
            np = (p[0] + v[0], p[1] + v[1])
            nb = grid.get(np)
            if nb:
                nbs.append((np, k))

    return nbs


# iterate over part 1 and 2
for part in [1, 2]:
    # Starting from (0,0) and 0 cost
    queue = [[0, (0, 0), "r", 0]]
    heapq.heapify(queue)
    # Cache for points we've already seen and branched from
    checked = {}
    # While there are points in the queue
    while queue:
        # get elements from the next item in the queue
        loss, point, moving, step_count = heapq.heappop(queue)
        # Check if it's already been seen
        if checked.get((point, moving, step_count)):
            continue
        # Add the current point, direction, and step_count to the cache
        checked[(point, moving, step_count)] = loss
        # Get valid surrounding points to check
        nbs = get_neighbors(point, moving, step_count, part)
        for c, d in nbs:
            # Calculate cumulative "cost" and steps for current point
            new_loss = int(grid[c]) + loss
            new_step_count = 1 if d != moving else step_count + 1
            # Add the current info to the queue to check again
            heapq.heappush(queue, [new_loss, c, d, new_step_count])
        # Sort queue in descending order to make sure the next step is the lowest cost
        # queue = sorted(queue, key=lambda x: x[-1], reverse=True)
    # destination point
    end = (len(lines) - 1, len(lines[0]) - 1)
    # get minimum cost of all checked spots that match the destination
    if part == 1:
        result = min(v for k, v in checked.items() if k[0] == end)
    if part == 2:
        result = min(v for k, v in checked.items() if k[0] == end and 4 <= k[2] <= 9)
    # Print result
    print(f"Part {part}: {result}")
