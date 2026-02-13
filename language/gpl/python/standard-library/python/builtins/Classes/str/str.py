# %%
# cast to string
import time

str(1)

# single quote
'single quotes allows "double quotes" inside'

# double quotes
"double quotes"

# triple quotes
"""Trip'le qu"oted
   Multiple lines"""

# nested quotes
"wrap lot's of other quotes"

# F-strings
name = "Henrique"
PI = 3.1415926535
f"Hey {name}, the value of π is {PI:.4f}"  # interpolation

foo = "ABC"
f"Bad nvram line: {foo!r}"

start_time = time.perf_counter()
print(f"Processing time: {time.perf_counter() - start_time}")

# Substituting
"hello %s" % "world"

# %%

# Concatenate
"12" + str(3)  # "123"

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
