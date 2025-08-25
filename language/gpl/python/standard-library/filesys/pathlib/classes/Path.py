# %%
# Introduced into Python 3.4 (2014)
from pathlib import Path

file_path = Path("./sample.txt")
file_path.read_text()
file_path.write_text("test")  # overwrite the file
