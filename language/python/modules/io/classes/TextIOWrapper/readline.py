# %%
import io

file: io.TextIOWrapper = open("file.txt", "r")

# readline returns an iterable over each line of the file
file.readline()
