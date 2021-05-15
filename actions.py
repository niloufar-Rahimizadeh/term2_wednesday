from data import *
import random

def select_word():
    index = random.randint(0, len(words)-1)
    return words[index]


def fill_result_word(word):
    global result_word
    for x in word:
        result_word.append("-")
    return result_word

def join_alphabet(list1):
    gussed_word = " ".join(list1)
    return gussed_word
