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


def load_input_lines(current_file):
    if current_file == "test":
        with open("../data/test.txt", "r") as f:
            lines = [l.replace("\n", "") for l in f.readlines()]
    else:
        day = current_file.split("\\")[-1].split(".")[0]
        input_path = f"../data/{day}.txt"
        with open(input_path, "r") as f:
            lines = [l.rstrip() for l in f.readlines()]

    return lines
