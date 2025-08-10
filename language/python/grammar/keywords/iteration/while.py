# %%
i = 1
while i <= 10:
    print(i)
    i += 1

# %%
i = 1
while i <= 10:
    print(i)
    i += 1

# %%

# Continue & Break
i = 1
while True:
    if i == 5:
        i += 1
        continue
    if i == 10:
        break
    print(i)
    i += 1

# %%
# Else is printed once when the while loop is exhausted
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Done")
