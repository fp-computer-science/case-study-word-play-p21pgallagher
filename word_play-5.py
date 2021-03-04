# Author: PJG (AMDG) 3/3/2021

def is_abecedarian(word):
    lst = list(word)
    abc = sorted(lst)
    if lst == abc:
        return True
    else:
        return False

word_choice = input("Input a word to see if it is abecedarian: ")

print(is_abecedarian(word_choice))
