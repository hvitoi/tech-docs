# %%
# Break out of a loop

for i in range(10):
    if i == 5:
        break
    print(i)

i = 0
while True:
    i += 1
    if i == 5:
        break
    print(i)
