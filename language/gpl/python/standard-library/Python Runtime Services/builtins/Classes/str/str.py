# %%
# cast to string
str(1)

# %%
# single quote
'single quotes allows "double quotes" inside'

# %%
# double quotes
"double quotes"

# nested quotes
"wrap lot's of other quotes"

# %%
# triple quotes
# It's mostly used for docstrings
# It's bad sometimes because it might cause unintended whitespaces due to the indentation
"""Trip'le qu"oted
   Multiple lines"""

# %%
# Python automatically concatenates adjacent string literals inside of parenthesis
# So unintended whitespaces!
message = (
    f"I am "
    f"multiline {str(1)} \n"
    f"Greetings! \n"
    "a b c d e f g h i j k l m n o p q r s t u v w x y z"
)
type(message)  # it's a string! not a tuple (tuples would need commas)

# %%
# F-strings
name = "Henrique"
PI = 3.1415926535
f"Hey {name}, the value of π is {PI:.4f}"  # interpolation

foo = "ABC"
f"Bad nvram line: {foo!r}"
f"{foo=}"

import time

start_time = time.perf_counter()
f"Processing time: {time.perf_counter() - start_time}"

# %%
# regex
r"Action\s*\d*\s*:[\s]*(.*?)"

# %%
# Substitution
"hello %s" % "world"

# %%
# Concatenate
"12" + str(3)  # "123"

# %%
# Multiply
"ab" * 2  # "abab"

# %%
# String slicing (just like lists)
my_str = "Henrique"
print(my_str[1:])

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

my_map = {"foo": "bar"}
str(my_map)  # convert map to string
