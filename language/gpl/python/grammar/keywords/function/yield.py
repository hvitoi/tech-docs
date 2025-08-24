# %%
# When "yield" is used in a function, the function execution turns into a generator (instead of the actual execution and the final result)
# With the function as a generator, the execution can pause and resume, instead of returning everything at once
# The function's state (local variables and execution point) is saved in the generator, so that when the iteration continues it resumes right after it had stopped before


def do_something():
    print("Executing the 1st part of the function")
    yield "🟡 1st part executed"
    print("Executing the 2nd part of the function")
    yield "🟡 2nd part executed"
    print("Executing the last part of the function")
    # An StopIteration exception is thrown here to signalize that the generator is exhausted
    # You could alternatively return a value manually force the StopIteration exception, in this case the return value can only be accessed within the exception
    # return "I am only accessible from a exception"


generator = do_something()  # at that point no code is run

try:
    print(next(generator))
    print(next(generator))
    print(next(generator))  # exception is thrown here
except StopIteration as err:
    print("✅ Done")
    # err is empty if the exception was cause by an end of function (not an return statement
    print(err)


# in a for-loop, the exception is handled transparently
for res in do_something():
    print(res)
print("✅ Done")

# %%


# Why use it?
# - Memory efficiency: Instead of creating a large list in memory, you can generate items one at a time.
# - Lazy evaluation: Values are produced only when needed.
# - Infinite sequences: You can represent streams or endless data without storing everything at once.


def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1


generator = infinite_counter()

next(generator)
next(generator)
next(generator)


# %%
# Returns a generator with lazy list of the values
# instead of the whole input at once (which might not fit in memory)
def get_column(csv: str):
    buffer = ""
    for char in csv:
        if char == ";":
            yield buffer
            buffer = ""
        else:
            buffer += char
    if buffer:  # Yield the last column if not empty
        yield buffer


csv = "col1;col2;col3"
lazy_columns = get_column(csv)

# The function is retriggered every time it is iterated over
# It stores internally a state to know which part has already been processed

next(lazy_columns)  # "col1"
next(lazy_columns)  # "col2"
next(lazy_columns)  # "col3"


# %%
class Database:
    def __init__(self):
        self.connection = "Connected!"


def get_db():
    db = Database()
    try:
        yield db
    finally:
        print("Closing DB connection")


lazy_db = get_db()
lazy_db
next(lazy_db)
# next(lazy_db) # fails! Because it has already reached the end of the function


# %%
def stream_my_file():
    with open("large-video-file.mp4", mode="rb") as file:
        yield from file


def stream_my_file2():
    with open("large-video-file.mp4", mode="rb") as file:
        for chunk in file:
            yield chunk  # same
