# Accepts expressions only

# %%
assert 1 == 1  # usa o operador de igualdade (__eq__) se definido
assert 1 != 2

# %%

# testa a identidade do objeto (se aponta exatamente para o objeto singleton None)
assert [] == None  # Throws! Although both are falsy, they are different objects
assert {} is {}  # Throws! Different objects

# Asserting constant literals is not recommended
assert 5 is 5  # literals (not objects) are equal (this behavior is not guaranteed!)
assert "foo" is "foo"

# %%
assert True  # Truthy
assert [0]  # Truthy

assert []  # Falsy
assert {}  # Falsy
assert ()  # Falsy
assert set()  # Falsy
assert range(0)  # Falsy
assert ""  # Falsy
assert 0  # Falsy
assert None  # Falsy
assert False  # Falsy
