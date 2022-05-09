# ---------------------------------------------------------
# Print variables
from math import *
print("Hello World")

name = "Henrique"
age = "35"
age_num = 35.23
is_male = True

print("There once was a man named " + name + ", he is " + age + " years old.")
# String interpolation
print(f"There once was a man named {name}, he is {age} years old.")
print("There once was a man named {}, he is {} years old.".format(name, age))

# entrada = input("Enter your name: ")    # Get input from User
#print("Hello " + entrada +"!")

# ---------------------------------------------------------
# If Statements

is_male = True
is_tall = True

if is_male and is_tall:
    print("You're a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not male but tall")
else:
    print("You are neither male nor tall")

# ---------------------------------------------------------
# Functions


def max_num(num1=10, num2=20, num3=30):          # Define default values
    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2

    else:
        return num3


res = max_num(1, 2, 3)                   # Call the function with parameters
res2 = max_num()                         # Call the function without parameters
print(f'The bigger number is {res}.')
print(f'The bigger number is {res2}.')

# ---------------------------------------------------------
# Lists
amigos = ["Amilton", "Bob", "Cassio"]
coisas = ["Eu", 2, True]

print(coisas[2])                    # Get element of the list
print(amigos[1:], amigos[:2])       # Get range of elements of the list

amigos.extend(coisas)               # Amigos receives coisas
print(amigos)

amigos.append("Dario")              # Append new item to amigos
print(amigos)

amigos.insert(0, "Zerilda")           # Insert into position 0
print(amigos)

amigos.remove("Zerilda")              # Remove item
amigos.remove(True)
del(amigos[4])                         # Remove by index
print(amigos)

amigos.pop()                        # Remove last item
print(amigos)

print(amigos.index("Amilton"))      # Index of the item
print(amigos.count("Eu"))           # Appearance of the item

amigos.sort()       # Asc
print(amigos)
amigos.reverse()    # Desc
print(amigos)

print(len(amigos))

amigos2 = amigos      # Copy
print(amigos2)

amigos.clear()      # Remove everything
print(amigos)

# -----------------------------------
# 2D List
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)

# ---------------------------------------------------------
# Touples
# Touples are constants, they cannot be changed
coordinates = (4, 5)
print(coordinates)
coordinates = [(4, 5), (6, 7), (80, 34)]

# -----------------------------------
# For Loops

pessoas = ["Maria", "Joao", "Cena"]
for pessoa in pessoas:
    print(pessoa)

for letra in "Eu sou Henrique":
    print(letra)

for index in range(10):     # 0 to 9
    print(index)

for index in range(1, 11):  # 1 to 10
    print(index)

for index in range(len(pessoas)):
    print(pessoas[index])

# ---------------------------------------------------------
# While Loops
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")


# ---------------------------------------------------------
# Dictionaries

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
}
print(monthConversions["Jan"])
print(monthConversions.get("Feb"))
print(monthConversions.get("Luv"))  # Returns none
print(monthConversions.get("Luv", "Not a valid key"))

del(monthConversions["Apr"])
print(monthConversions)

# ---------------------------------------------------------
# String operations
print("Giraffe\nAcademy")
frase = "Giraffe Academy"
print(frase.lower())
print(frase.upper())
print(frase.isupper())
print(frase.upper().isupper())

print(len(frase))
print(frase[0])
print(frase.index("r"))
print(frase.index("iraf"))

print(frase.replace("Giraffe", "Elephant"))
print(frase)

# ---------------------------------------------------------
# Number operations

print(-2.09)
print(3 / 2)
print(10 % 3)

num = 5
print("My favorite number is " + str(num))

print(abs(num))
print(pow(2, 3))
print(max(4, 6))
print(min(4, 6))
print(round(3.7))

# math library
print(floor(3.6))
print(ceil(4.2))
print(sqrt(36))

print(int(35.6))


# -----------------------------------
# Try Except

try:
    value = 10/0
    number = int("texto nao eh numero")
    print(number)
except ValueError as err:  # err guarda o erro
    print("Invalid Input")
    print(err)
except ZeroDivisionError as err:
    print("Divisao por 0")
    print(err)


# -----------------------------------
# Classes and Objects

class Estudante:
    def __init__(self, name, major, gpa, is_on_probation):  # self is the own object
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):        # Pass the object to the function
        if self.gpa >= 3.5:
            return True
        else:
            return False

    school = "UFJF"         # Class variable


# Instance of a class. An object
estudante1 = Estudante("Jim", "Business", 3.1, False)
estudante2 = Estudante("Maria", "Engineering", 4.2, True)
print(estudante1.name)
print(estudante2.on_honor_roll())
estudante1.age = 26             # New variables can be added on fly
print(estudante1.age)
print(Estudante.school)


class Questao:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Questao("Que cor é a maca", "a"),
    Questao("Que cor é a banana", "c"),
    Questao("Que cor é a laranja", "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You scored" + str(score) + "/" + str(len(questions)))

# run_test(questions)


# -----------------------------------
# Inheritance

class Chef:
    def make_chicken(self):
        print("Makes chicken")

    def make_salad(self):
        print("Makes salad")

    def make_special_dish(self):
        print("Makes bbq")


myChef = Chef()
myChef.make_chicken()


class ChineseChef(Chef):  # use all the functions inside of the chef class
    def make_fried_rice(self):
        print("Makes fried rice")

    def make_special_dish(self):  # Overwrites the original function
        print("Makes orange chicken")


myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()
