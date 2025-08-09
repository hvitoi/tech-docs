# %%
import io

# %%
# Overwrite the entire file
# Creates a new file if not exists
file: io.TextIOWrapper = open("file.txt", "w")  # opens itself
file.write("abc")
file.close()  # close to save

# %%
# Append
file = open("file.txt", "a")
file.write("\nToby - Human Resources")
file.write("\nKelly - Customer Service")
file.close()
