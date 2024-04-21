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
