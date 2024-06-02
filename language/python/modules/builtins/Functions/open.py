#
open("file.txt", "r")  # read
open("file.txt", "rb")  # read binary
open("file.txt", "w")  # write
open("file.txt", "wb")  # write binary
open("file.txt", "a")  # append
open("file.txt", "r+")  # read and write
file = open("file.txt", "r")

#
with open("file. txt") as f:
    for line in f:
        print(line)
