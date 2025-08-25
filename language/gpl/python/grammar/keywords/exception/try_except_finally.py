# %%
try:
    value = 10 / 0
    number = int("texto nao eh numero")
    print(number)
except ValueError as err:  # err guarda o erro
    print("Invalid Input")
    print(err)
except ZeroDivisionError as err:
    print("Divisao por 0")
    print(err)
    raise  # re-raise the same exception. If this case the "finally" block is executed before raising
finally:
    print("Done")

# %%
# Handling exception groups with "except*"
from builtins import ExceptionGroup

ex_group = ExceptionGroup("Multiple errors", [ValueError("bad"), TypeError("wrong")])

try:
    raise ex_group
except* ValueError as err:
    print("Caught:", err.exceptions)
except* TypeError as err:
    print("Caught:", err.exceptions)
