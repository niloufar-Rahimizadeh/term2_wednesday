from data import *
from actions import *


selected_word = select_word()

list1 = ['-']*len(selected_word)


faild_counter = 0

while faild_counter<7:
    guessed_alphabet = input("Please enter your alphabet: ")
    w = find_alphabet(list1, guessed_alphabet, selected_word)
    v = join_alphabet(w)