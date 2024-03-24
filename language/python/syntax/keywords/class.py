# %%
class Student:
    # attributes
    school = "UFJF"  # class attribute
    number_of_students = 0  # class attribute

    # constructor
    # python does not allow multiple constructors (with multiple signatures), instead you can define default values for each argument
    def __init__(self, name, major):  # self is the object instance
        Student.number_of_students += 1  # increase a static attribute
        self.name = name  # instance attribute
        self.major = major  # instance attribute

    # methods
    def show(self):
        print(f"{self.name} studies {self.major}")

    @classmethod
    def show_number_of_students(cls):  # receives the class itself
        print(f"There are {cls.number_of_students} matriculated at {cls.school}")

    @staticmethod
    def say_hello(person):  # knows nothing about the class/instance
        print(f"Hello, {person}!")


# Instance of a class. An object
student1 = Student("Jim", "Business")
student2 = Student("Maria", "Engineering")

student1.show()
student2.show()

Student.show_number_of_students()
Student.say_hello("Maria")


# %%
# Inheritance


class Chef:
    def __init__(self, name):
        self.name = name

    def make_chicken(self):
        print(f"{self.name} makes chicken")

    def make_salad(self):
        print("f{self.name} makes salad")

    def make_special_dish(self):
        print(f"{self.name} makes bbq")


my_chef = Chef("Jose")
my_chef.make_chicken()


class ChineseChef(Chef):
    # inherits all the functions from the Chef class (including the constructor)
    def make_fried_rice(self):
        print(f"{self.name} makes fried rice")

    # Overwrites the original function
    def make_special_dish(self):
        print(f"{self.name} makes orange chicken")


my_chinese_chef = ChineseChef("Zhang")
my_chinese_chef.make_chicken()
my_chinese_chef.make_fried_rice()
my_chinese_chef.make_special_dish()


class ItalianChef(Chef):
    # overwrite the constructor
    def __init__(self, name):
        super().__init__(name)
        self.name = self.name + "🇮🇹"

    def make_pizza(self):
        print(f"{self.name} makes pizza")


my_italian_chef = ItalianChef("Luigi")
my_italian_chef.make_pizza()


class AmericanChef(Chef):
    # Just use the parent class unchanged
    pass


my_american_chef = AmericanChef("John")
my_american_chef.make_chicken()
