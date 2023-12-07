# %%
from playground import *
from collections import Counter

lines = load_input_lines("test")
lines = load_input_lines(__file__)


class PokerGame:
    def __init__(self, hands):
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
        self.card_order_p1 = {
            "A": "00",
            "K": "01",
            "Q": "02",
            "J": "03",
            "T": "04",
            "9": "05",
            "8": "06",
            "7": "07",
            "6": "08",
            "5": "09",
            "4": "10",
            "3": "11",
            "2": "12",
        }
        self.card_order_p2 = {
            "A": "00",
            "K": "01",
            "Q": "02",
            "T": "03",
            "9": "04",
            "8": "05",
            "7": "06",
            "6": "07",
            "5": "08",
            "4": "09",
            "3": "10",
            "2": "11",
            "J": "12",
        }
        self.categorized_p1 = {i: {} for i in self.hand_ranks.values()}
        self.categorized_p2 = {i: {} for i in self.hand_ranks.values()}
        self._categorize_p1()
        self._categorize_p2()

    def _categorize_p1(self):
        for card, bet in self.hands:
            c = Counter(card)
            r = self.hand_ranks[tuple(sorted(c.values()))]
            mapped_card = "".join(self.card_order_p1[i] for i in card)
            self.categorized_p1[r][mapped_card] = bet

    def _categorize_p2(self):
        for card, bet in self.hands:
            c = Counter(card)
            print(c)
            temp_c = []
            if "J" in c.keys() and "".join(c.keys()) != "J":
                temp_c = self.make_best_hand(c)
            use_c = c if not temp_c else temp_c
            print(use_c)
            r = self.hand_ranks[tuple(sorted(use_c.values()))]
            mapped_card = "".join(self.card_order_p2[i] for i in card)
            self.categorized_p2[r][mapped_card] = bet

    def make_best_hand(self, c):
        # extract J value
        j = c["J"]
        # remove J from counter
        del c["J"]
        # add J value to highest count left
        c[max(c, key=c.get)] = c[max(c, key=c.get)] + j
        # Return counter
        return c

    def calculate_score(self, hands, part):
        ranked_hands = []
        for i, hs in hands:
            if hs:
                ho = sorted(hs, reverse=True)
                for h in ho:
                    ranked_hands.append(hs[h])
        p1 = 0
        for i, bet in enumerate(ranked_hands):
            p1 += (i + 1) * bet
        print(f"Part {part}: {p1}")

    def solve(self):
        self.calculate_score(hands=self.categorized_p1.items(), part=1)
        self.calculate_score(hands=self.categorized_p2.items(), part=2)


PokerGame(lines).solve()
