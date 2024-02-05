# Function with default parameters
def sumNums(num1=10, num2=20, num3=30):
    return num1 + num2 + num3


# Types are optional
def subtractNums(num1: int = 10, num2: int = 20, num3: int = 30) -> int:
    return num1 - num2 - num3


sumNums(1, 2, 3)
sumNums()  # take default values
subtractNums()


# yield is another kind of "return"
def my_movie_splitter(line):
    (userId, movieId, rating, timestamp) = line.split("\t")
    yield userId, movieId
