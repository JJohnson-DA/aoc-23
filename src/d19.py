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
        self.checks = []
        self.fallback = None

        for q in qs:
            x = q.split(":")
            if len(x) > 1:
                l = x[0][0]
                c = "pn" + x[0][1:]
                d = x[1]
                self.checks.append([l, c, d])
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
            for l, c, d in flow.checks:
                if match_found or self.next in "AR":
                    break
                pn = self.nums[l]
                if eval(c):
                    self.next = d
                    match_found = True
                    break
            if not match_found:
                self.next = flow.fallback
        if self.next == "A":
            return sum(self.nums.values())
        else:
            return 0


parts = [Part(p) for p in parts]
flows = {f.id: f for f in [Workflow(w) for w in workflows]}
print(f"Part 1: {sum(p.check_workflows(flows) for p in parts)}")
