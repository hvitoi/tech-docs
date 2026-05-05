# %%
import string
import random

string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

"".join(random.choices(string.ascii_uppercase + string.digits, k=5))
