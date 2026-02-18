# %%
# Removes whitespaces
"   Hey!   ".strip()
"\nHey!".strip("\n")  # removes new lines

# %%
# alternative (to any kind of iterable)
my_str = "   Hey!   "

# strip left
while my_str[0] == " ":
    my_str = my_str[1:]

# strip right
while my_str[-1] == " ":
    my_str = my_str[:-1]

my_str

# %%
# alternative (to any kind of iterable)
my_str = "   Hey!   "

# strip left
for i in range(len(my_str)):
    if my_str[i] != " ":
        break
left = i

for i in reversed(range(len(my_str))):
    if my_str[i] != " ":
        break
right = i

my_str[left : right + 1]
