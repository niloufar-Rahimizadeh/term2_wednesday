from data import *
from actions import *


selected_word = select_word()

a =fill_result_word(selected_word)

print(join_alphabet(a))
inp = input("PL")
out = find_alphabet(a, inp, selected_word)
print(out)