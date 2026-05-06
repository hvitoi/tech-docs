# %%
# What can live at class scope:
#   - class attribute      : value bound at class body, shared across instances
#   - instance attribute   : value bound on `self`, one per instance
#   - instance method      : function with `self`
#   - classmethod          : function with `cls` (decorated)
#   - staticmethod         : plain function (decorated, no self/cls)
#   - property             : computed attribute (decorated)


class Student:
    # === class attributes (shared across instances) ===
    school = "UFJF"  # default value, can be shadowed per-instance
    city: str  # annotation only — no value bound; must be set on the instance
    count = 0  # shared counter

    # === __init__: a magic method, called when constructing the instance ===
    def __init__(self, name: str, major: str, age: int = 22):
        Student.count += 1  # bump the shared counter
        self.name = name  # instance attribute
        self.major = major
        self._gpa = 0.0  # single underscore — "private" by convention
        self.__age = age  # double underscore — name-mangled to _Student__age
        self.school = "USP"  # shadows the class attribute on THIS instance only

    # === instance method — receives self ===
    def show(self) -> None:
        print(f"{self.name} studies {self.major}")

    # === property — accessed like an attribute, no parentheses ===
    @property
    def is_adult(self) -> bool:
        return self.__age >= 18

    # === classmethod — receives the class ===
    @classmethod
    def total(cls) -> int:
        return cls.count

    # === staticmethod — no self, no cls ===
    @staticmethod
    def is_valid_major(major: str) -> bool:
        return len(major) > 0

    # === other magic methods: __str__ used by print(), __repr__ by the REPL ===
    def __str__(self) -> str:
        return f"{self.name} ({self.major})"


jose = Student("Jim", "Business")
maria = Student("Maria", "Engineering")

print(jose)  # "Jim (Business)"           ← __str__
jose.show()  # "Jim studies Business"     ← instance method
jose.is_adult  # True                     ← property, no parentheses
Student.total()  # 2                     ← classmethod
Student.is_valid_major("CS")  # True     ← staticmethod

# attribute lookup: instance first, then class
Student.school  # "UFJF"  — class attribute
jose.school  # "USP"       — shadowed in __init__
# Student.city            # AttributeError — annotation only, never assigned

# private / name-mangled
# jim.__age               # AttributeError — name-mangled
jose._Student__age  # type: ignore  # 22 — accessible via the mangled name (don't do this!)


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

# %%

# Composition


class Engine:
    def start(self):
        print("Vruuumm")


class Car:
    def __init__(self):
        self.model = "VW Gol"
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Driving around!")


my_car = Car()
my_car.drive()
