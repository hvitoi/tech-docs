# %%
# ZeroDivisionError -- ArithmeticError -- Exception -- BaseException
#
# Second argument of a division or modulo is zero.

1 / 0  # ZeroDivisionError: division by zero
1 // 0  # ZeroDivisionError: integer division or modulo by zero
1 % 0  # ZeroDivisionError: integer modulo by zero
divmod(1, 0)  # ZeroDivisionError

# Float division by zero also raises (NOT inf/nan, unlike NumPy)
1.0 / 0.0  # ZeroDivisionError

# %%
# Catch ArithmeticError to also catch OverflowError and FloatingPointError
try:
    1 / 0
except ArithmeticError:
    pass

# %%
# NumPy semantics differ -- it returns inf/nan and emits a warning instead.
# import numpy as np
# np.float64(1) / np.float64(0)   # inf, RuntimeWarning
