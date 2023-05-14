# Function with default parameters
def max_num(num1=10, num2=20, num3=30):
    return num1 + num2 + num3


max_num(1, 2, 3)
max_num()  # take default values


# yield is another kind of "return"
def my_movie_splitter(line):
    (userId, movieId, rating, timestamp) = line.split('\t')
    yield userId, movieId


# def from lambda
def squarer(num): return num*num
