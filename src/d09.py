# %%
from playground import load_input_lines

lines = load_input_lines(__file__)


class NextInt:
    def __init__(self, line, part_2):
        self.factor = -1 if part_2 else 1
        self.sequence = [[int(x) for x in line.split()]]
        self.parsed = self._parse_sequence(self.sequence)

    def _add_line(self, seq):
        new_seq = [seq[-1][i + 1] - seq[-1][i] for i in range(len(seq[-1]) - 1)]
        seq.append(new_seq)
        return seq

    def _parse_sequence(self, sequence):
        seq = sequence.copy()
        while not all([s == 0 for s in seq[-1]]):
            seq = self._add_line(seq)
        return [s[:: self.factor] for s in seq]

    def add_digits(self):
        parsed = self.parsed.copy()
        for i in range(-1, -(len(parsed)), -1):
            digit = parsed[i - 1][-1] + (parsed[i][-1] * self.factor)
            parsed[i - 1].append(digit)

        return parsed

    def get_digit(self, part_2=False):
        return self.add_digits()[0][-1]


print(f"Part 1: {sum([NextInt(l, False).get_digit() for l in lines])}")
print(f"Part 2: {sum([NextInt(l, True).get_digit() for l in lines])}")
