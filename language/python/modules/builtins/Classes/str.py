# %%
# cast to string
str(1)

# single quote
'single quotes allows "double quotes" inside'

# double quotes
"double quotes"

# nested quotes
"wrap lot's of other quotes"

# %%
# interpolation
name = "John"
age = 21
f"There once was a man named {name}, he is {age} years old."


# %%
# Colors
RESET_ALL = 0
BRIGHT = 1
DIM = 2
BLINK = 5
NORMAL = 22
NBLINK = 25
BLACK = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
WHITE = 37


def pprint(text, options):
    formatting_code = ";".join(map(str, options))
    print(f"\033[{formatting_code}m{text}")


pprint("Hello!", (BRIGHT, RED))

# %%
myStr: str = "Henrique"
print(myStr[1:])  # strings function like lists

# %%
assert "abc"
assert ""  # fails! empty strings are Falsy

# %%
"12" + str(3)
