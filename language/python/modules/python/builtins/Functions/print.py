# Simple usage
name = "John"
age = 21
print("Hello World")
print("Hello " + name + "!" + " You are " + str(age) + " years old.")
print(f"There once was a man named {name}, he is {age} years old.")
print(
    "There once was a man named {name}, he is {age} years old.".format(
        name=name, age=age
    )
)

# Triple quotes
print("""Trip'le qu"oted""")
print("""Ag'ain qu"oted""")
