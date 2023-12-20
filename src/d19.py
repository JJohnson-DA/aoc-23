# %%
from playground import *
import re

with open("../data/d19.txt", "r") as f:
    workflows, parts = f.read().split("\n\n")

workflows = workflows.split("\n")
parts = parts.split("\n")


class Workflow:
    def __init__(self, workflow) -> None:
        id, quals = workflow.split("{")
        qs = quals.split(",")
        self.id = id
        self.checks = {}
        self.fallback = None

        for q in qs:
            x = q.split(":")
            if len(x) > 1:
                l = x[0][0]
                if l not in self.checks.keys():
                    self.checks[l] = []
                    self.checks[l].append(["pn" + x[0][1:], x[1]])
                else:
                    self.checks[l].append(["pn" + x[0][1:], x[1]])
            if len(x) == 1:
                self.fallback = x[0].replace("}", "")


class Part:
    def __init__(self, item) -> None:
        nums = re.findall("\d+", item)
        self.nums = {}
        self.nums["x"] = int(nums[0])
        self.nums["m"] = int(nums[1])
        self.nums["a"] = int(nums[2])
        self.nums["s"] = int(nums[3])
        self.next = "in"

    def check_workflows(self, flows):
        while self.next not in "AR":
            flow = flows[self.next]
            match_found = False
            for l, v in flow.checks.items():
                if match_found or self.next in "AR":
                    break
                pn = self.nums[l]
                for c, d in v:
                    if eval(c):
                        self.next = d
                        match_found = True
                        # break
            if not match_found:
                self.next = flow.fallback
        if self.next == "A":
            return sum(self.nums.values())
        else:
            return 0


parts = [Part(p) for p in parts]
flows = {f.id: f for f in [Workflow(w) for w in workflows]}
# parts[11].check_workflows(flows['vhb'])
sum(p.check_workflows(flows) for p in parts)

# 377962 too high
# 362013 too high
# 327646 not right
# 342727 not right
# 329616 not right
# 354108 not right
# 345108 not right
