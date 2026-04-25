# %%
from glob import glob

for glob_match in glob("/home/hv/*rc"):
    print(glob_match)
