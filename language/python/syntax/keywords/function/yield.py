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
