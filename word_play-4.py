# Author: PJG (AMDG) 3/3/2021

def uses_only(letters, word):
    num_of_words = 0
    if letters in word:
        num_of_words += 1
    else:
        num_of_words += 0
    return num_of_words

a_letters = input("Write a string of allowed letters:")

print(a_letters, "words.txt")
