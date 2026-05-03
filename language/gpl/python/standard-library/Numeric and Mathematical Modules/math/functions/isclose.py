# %%

import math

0.1 + 0.2 == 0.3  # False  (it's 0.30000000000000004)
math.isclose(0.1 + 0.2, 0.3)  # True

# %%

math.isclose(1e-12, 0)  # False
math.isclose(1e-12, 0, abs_tol=1e-9)  # True
