# Author: PJG (AMDG) 3/3/2021

def avoid(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False

forbidden = input("What are your forbidden letters? ")

with open("Words.txt") as new_file:
    words = new_file.readlines()

    for line in words:
        if avoid(line, forbidden):
            print(line)