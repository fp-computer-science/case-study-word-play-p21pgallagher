# Author: PJG (AMDG) 3/3/2021

def no_e(word):
    if "e" not in word:
        return True
    return False

with open("words.txt") as file1, open("words_without_e.txt", "w") as file2:
    for line in file1.readlines():
        if no_e(line):
            file2.write(line)
        else:
            continue

with open("words.txt") as new_text, open("words_without_e.txt", "w") as no_e_text:
    all_words = len(new_text.readlines())
    no_e_total = len(no_e_text.readlines())

    percent = (no_e_total / all_words) * 100
    print(percent + "percent of words in 'words.txt' have no e")