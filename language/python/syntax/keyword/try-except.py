
# -----------------------------------
# Try Except

try:
    value = 10/0
    number = int("texto nao eh numero")
    print(number)
except ValueError as err:  # err guarda o erro
    print("Invalid Input")
    print(err)
except ZeroDivisionError as err:
    print("Divisao por 0")
    print(err)
