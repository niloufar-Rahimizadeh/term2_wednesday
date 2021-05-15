import random

list1 =["horse", "tiger", "computer", "oven", "honey"]


def select_word(): 
    index = random.randint(0, len(list1)-1)
    return list1[index]

a = select_word()
print(a)