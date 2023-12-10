# %%
import inflect
from word2number import w2n
import platform


def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)


def words_to_number(words):
    try:
        return w2n.word_to_num(words)
    except ValueError:
        print(f"Error: Unable to convert words to number: '{words}'")
        return None


def load_lines(current_file):
    if current_file == "test":
        with open("../data/test.txt", "r") as f:
            lines = [l.replace("\n", "") for l in f.readlines()]
    else:
        if "mac" in platform.platform():
            split_char = "/"
        else:
            split_char = "\\"
        day = current_file.split(split_char)[-1].split(".")[0]
        input_path = f"../data/{day}.txt"
        with open(input_path, "r") as f:
            lines = [l.rstrip() for l in f.readlines()]

    return lines
