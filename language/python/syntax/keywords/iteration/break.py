# %%
# Break out of a for loop
for i in range(10):
    if i == 5:
        break
    print(i)

# %%
# Break out of a while loop
i = 0
while True:
    if i == 5:
        break
    print(i)
    i += 1

# %%
for i in range(5):
    for j in range(5):
        if j == 2:
            break  # break out of the inner for only
        print(i, j)
