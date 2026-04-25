# %%
class Person:
    first_name: str

    def __init__(self, name):
        self.first_name = name


p1 = Person("Henrique")


# Get an attribute out of an object/class (not dict)
getattr(p1, "first_name")  # same as p1.first_name
p1.first_name
getattr(p1, "last_name", "Not Found")  # returns the default argument
