# %%
import random
from unittest.mock import patch

# temporarily replaces (“patches”) an object in a module with a mock

with patch("random.randint", return_value=9):
    print(random.randint())


print(random.randint(1, 10))  # original behavior
