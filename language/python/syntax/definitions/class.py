class Estudante:
    # constructor
    def __init__(self, name, major, gpa, is_on_probation):  # self is object instance
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    # method
    def on_honor_roll(self):
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
