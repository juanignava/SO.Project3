import sys

file = open("test.txt")

line = file.readline()

counter = 0
while (line != ""):
    if (line == '\n'):
        line = file.readline()
        counter += 1
        continue
    print("line number: ", counter)
    print(line)
    line = file.readline()
    counter += 1