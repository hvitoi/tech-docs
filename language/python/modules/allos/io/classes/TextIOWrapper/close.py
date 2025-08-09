# %%
import io

file: io.TextIOWrapper = open("file.txt", "w")  # opens itself

file.write("abc")
file.close()  # close to save
