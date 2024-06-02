#
open("file.txt", "r")  # read
open("file.txt", "w")  # write
open("file.txt", "a")  # append
open("file.txt", "r+")  # read and write
file = open("file.txt", "r")

#
with open("file. txt") as f:
    for line in f:
        print(line)
