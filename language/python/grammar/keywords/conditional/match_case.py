# %%
# pattern matching was introduced in Python 3.10

num = 10

match num:
    case 10:
        print("It's 10")
    case 5:
        print("It's 5")
    case _:
        print("It's something else")
