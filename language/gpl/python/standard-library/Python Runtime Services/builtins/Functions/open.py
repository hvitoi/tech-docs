# %%
#
from io import TextIOWrapper


open("file.txt", mode="r")

open("file.txt", "r")  # read
open("file.txt", "rb")  # read binary

open("file.txt", "w")  # write
open("file.txt", "wb")  # write binary

open("file.txt", "a")  # append
open("file.txt", "r+")  # read and write


file: TextIOWrapper = open("file.txt", "r")

# %%
# Read
with open("file.txt") as f:
    for line in f:
        print(line)

# %%
# Write
# %%
with open("file.txt", "w") as file:
    file.write("foo")
