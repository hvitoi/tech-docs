# Function with default parameters
def sum_nums(num1=10, num2=20, num3=30):
    """
    This function does X
    """
    return num1 + num2 + num3


# Types are optional
def subtract_nums(num1: int = 10, num2: int = 20, num3: int = 30) -> int:
    return num1 - num2 - num3


sum_nums(1, 2, 3)
sum_nums()  # take default values
subtract_nums()


# yield is another kind of "return"
def my_movie_splitter(line):
    (userId, movieId, rating, timestamp) = line.split("\t")
    yield userId, movieId
