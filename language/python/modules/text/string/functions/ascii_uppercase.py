# %%
import string
import random

# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_uppercase

"".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
