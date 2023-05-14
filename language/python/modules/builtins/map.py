
foo = [1, 2, 3]


def squarer(num):
    return num*num


map(squarer, foo)  # map object
map(lambda num: num**2, foo)  # map object

list(map(lambda num: num**2, foo))
