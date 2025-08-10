# %%
def func1():
    a = 1


func1()
print(a)  # fail! try to access variable from inner scope

# %%
a = 1


def func2():
    print(a)


func2()  # ok. Access variable from outer scope


# %%
a = 1


def func3():
    a = a + 1  # fail! Cannot modify variable from outer scope


func3()


# %%
a = 1


def func4():
    global a
    a = a + 1
    print(a)


func4()  # ok (although not recommended). Can modify variable from outer scope with global keyword


# %%
def hello():
    for _ in range(3):
        message = "Hello!"
    print(message)  # accessible! Even though it was created inside of the for loop
    # Python has function-level scope — variables created anywhere inside a function are accessible anywhere else inside that function.
    # Blocks like loops (for, while) and conditionals (if) do NOT create new scopes.


hello()
