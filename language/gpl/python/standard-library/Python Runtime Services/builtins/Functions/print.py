# %%
name = "John"
age = 21
print("Hello World")
print("Hello World")
print("""Trip'le qu"oted""")
print("Hello " + name + "!" + " You are " + str(age) + " years old.")
print(f"There once was a man named {name}, he is {age} years old.")
print(
    "There once was a man named {name}, he is {age} years old.".format(
        name=name, age=age
    )
)
# print("a" "b")  # multiple strings
print("a", "b")  # joined by space
