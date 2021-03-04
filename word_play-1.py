# Author: PJG (AMDG) 3/3/2021

file1 = open("words.txt", "r")
while True:
    line = file1.readline()
    if len(line) < 20:
        with open("greater_than20.txt", "a") as file2:
            file2.write(line)
    else:
        continue
file1.close()
