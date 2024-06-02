# %%
import io

file: io.TextIOWrapper = open("read.py", "r")  # opens itself

file.read()
