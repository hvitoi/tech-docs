# %%
# Creates an Iterator object

range(10)  # 0 to 9
range(1, 11)  # 1 to 10
range(1, 11, 2)  # 1, 3, 5, 7, 9

for i in range(5):
    print(i)

for i in range(5).__reversed__():
    print(i)

# %%
# Make a list out of a range

list(range(5))
