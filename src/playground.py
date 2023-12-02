# %%
import inflect
from word2number import w2n


def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)


def words_to_number(words):
    try:
        return w2n.word_to_num(words)
    except ValueError:
        print(f"Error: Unable to convert words to number: '{words}'")
        return None
