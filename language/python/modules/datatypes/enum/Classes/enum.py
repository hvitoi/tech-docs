# %%
from enum import Enum


# The Enum value is Any
class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


Color.RED

# %%


# The Enum value needs to be "str"
class AIModel(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


model = AIModel("alexnet")
AIModel.alexnet

assert model is AIModel.alexnet
assert model.value == "alexnet"
