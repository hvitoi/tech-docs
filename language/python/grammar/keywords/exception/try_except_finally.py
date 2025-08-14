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
