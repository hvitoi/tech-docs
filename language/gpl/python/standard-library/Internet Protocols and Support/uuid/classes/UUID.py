# %%
import random
import uuid

uuid.UUID("12345678-1234-5678-1234-567812345678")  # your seed UUID
uuid.UUID(int=0)  # 00000000-0000-0000-0000-000000000000

# %%
seed = random.Random("abc")
uuid.UUID(int=seed.getrandbits(128), version=4)

# %%
import hashlib

uuid.UUID(bytes=hashlib.md5(b"abc").digest(), version=4)
