# %%
import io

file: io.TextIOWrapper = open("file.txt", "r")

file.read()

# True for "r" and False for "w"
file.readable()
