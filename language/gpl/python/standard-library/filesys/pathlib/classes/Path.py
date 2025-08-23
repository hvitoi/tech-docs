# %%
from pathlib import Path

file_path = Path("./sample.txt")
file_path.read_text()
file_path.write_text("test")  # overwrite the file
