# %%
class Student:
    # attributes
    school = "UFJF"  # class/instance attribute
    city: str  # class/instance attribute (just a placeholder, it still needs to be instantiated)
    number_of_students = 0  # class/instance attribute

    # constructor
    # python does not allow multiple constructors (with multiple signatures), instead you can define default values for each argument
    def __init__(self, name, major):  # self is the object instance
        Student.number_of_students += 1  # increase a class attribute
        self.name = name  # instance attribute
        self.major = major  # instance attribute
        self.__age = 22  # a private instance attribute
        self.school = "USP"  # overrides the value of the class/instance attribute for that specific instance only!

    # def __init__(self): # default/empty constructor is automatically used if you don't specify any
    #     pass

    # methods
    def show(self):
        print(f"{self.name} studies {self.major}")

    # private methods (single underscore): intended to be private to the module or class (a convention only)
    def _show(self):
        print(f"{self.name} studies {self.major}")

    # name mangling (double underscore): python rewrites the function/attribute names to avoid naming conflicts in subclasses. It's renamed to _MyClass__myvar
    def __show(self):
        print(f"{self.name} studies {self.major}")

    # "magic methods": reserved for Python's internal use
    # __init__, __str__, __repr__, __call__
    def __str__(self):
        return f"[Name: {self.name}; Major: {self.major}"

    # Class Methods receives the class itself
    @classmethod
    def show_number_of_students(cls):
        print(f"There are {cls.number_of_students} matriculated at {cls.school}")

    # Static Methods know nothing about the class or instance
    @staticmethod
    def say_hello(person):
        print(f"Hello, {person}!")


# Instance of a class. An object
student1 = Student("Jim", "Business")
student11 = Student(name="Jim", major="Business")  # same
student2 = Student("Maria", "Engineering")

# toString method
print(student1)
print(student2)

# show method
student1.show()
student2.show()

Student.show_number_of_students()
Student.say_hello("Maria")

# Class attributes
Student.school  # UFJF
student1.school  # USP (because it was overwritten in the constructor)
# Student.city  # fails! It has not be instantiated

# Instance attributes
student1.major  # Business
# Student.major  # fails! it's not a class attribute
# student1.__age  # fails! Private attribute


# %%
# Inheritance


class Chef:
    def __init__(self, name):
        self.name = name

    def make_salad(self):
        print(f"{self.name} makes salad")

    def make_special_dish(self):
        print(f"{self.name} has not special dish")


my_chef = Chef("Jose")
my_chef.make_salad()


class ChineseChef(Chef):
    # Child classes that do not define a constructor automatically have a empty constructor calling the constructor of the super class

    # inherits all the functions from the Chef class (including the constructor)
    def make_fried_rice(self):
        print(f"{self.name} makes fried rice 🇨🇳")

    # Overwrites the original function
    def make_special_dish(self):
        print(f"{self.name} makes orange chicken 🇨🇳")


my_chinese_chef = ChineseChef("Zhang")
my_chinese_chef.make_salad()
my_chinese_chef.make_fried_rice()
my_chinese_chef.make_special_dish()


class ItalianChef(Chef):
    # overwrite the constructor
    def __init__(self, name):
        super().__init__(name)  # super refers to the parent class (not instance)
        self.name = self.name + "🤌"

    def make_pizza(self):
        print(f"{self.name} makes pizza 🇮🇹")


my_italian_chef = ItalianChef("Luigi")
my_italian_chef.make_pizza()


class AmericanChef(Chef):
    # Just use the parent class unchanged
    # Default constructors using the super class constructor is used
    pass


my_american_chef = AmericanChef("John")
my_american_chef.make_salad()
