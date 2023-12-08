# %%
from playground import *
from collections import Counter

lines = load_input_lines("test")


class PokerGame:
    def __init__(self, hands, part):
        self.part = part
        self.hands = [
            (card, int(bet)) for card, bet in [line.split() for line in hands]
        ]
        self.hand_ranks = {
            (1, 1, 1, 1, 1): 1,  # high card
            (1, 1, 1, 2): 2,  # pair
            (1, 2, 2): 3,  # two pair
            (1, 1, 3): 4,  # three of a kind
            (2, 3): 5,  # full house
            (1, 4): 6,  # four of a kind
            (5,): 7,  # five of a kind
        }
        self.card_order = {
            "A": ["00", "00"],
            "K": ["01", "01"],
            "Q": ["02", "02"],
            "J": ["03", "12"],
            "T": ["04", "03"],
            "9": ["05", "04"],
            "8": ["06", "05"],
            "7": ["07", "06"],
            "6": ["08", "07"],
            "5": ["09", "08"],
            "4": ["10", "09"],
            "3": ["11", "10"],
            "2": ["12", "11"],
        }
        self.categorized = {i: {} for i in self.hand_ranks.values()}
        self._categorize(self.part)

    def _categorize(self, part):
        for card, bet in self.hands:
            c = Counter(card)
            if part == 2:
                temp_c = []
                if "J" in c.keys() and "".join(c.keys()) != "J":
                    temp_c = self.make_best_hand(c)
                c = c if not temp_c else temp_c
            r = self.hand_ranks[tuple(sorted(c.values()))]
            mapped_card = "".join(self.card_order[i][self.part - 1] for i in card)
            self.categorized[r][mapped_card] = bet

    def make_best_hand(self, c):
        j = c.pop("J")
        c[max(c, key=c.get)] = c[max(c, key=c.get)] + j
        return c

    def calculate_score(self):
        ranked_hands = []
        for i, hs in self.categorized.items():
            if hs:
                ho = sorted(hs, reverse=True)
                for h in ho:
                    ranked_hands.append(hs[h])
        score = 0
        for i, bet in enumerate(ranked_hands):
            score += (i + 1) * bet
        print(f"Part {self.part}: {score}")


for part in [1, 2]:
    PokerGame(lines, part).calculate_score()
