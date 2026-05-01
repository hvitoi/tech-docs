# %%
def fizzbuzz(n: int) -> list:
    arr = []

    for el in range(1, n + 1):
        if el % 3 == 0 and el % 5 == 0:
            arr.append("fizzbuzz")
            continue
        if el % 3 == 0:
            arr.append("fizz")
            continue
        if el % 5 == 0:
            arr.append("buzz")
            continue
        arr.append(el)
    return arr


assert fizzbuzz(5) == [1, 2, "fizz", 4, "buzz"]
