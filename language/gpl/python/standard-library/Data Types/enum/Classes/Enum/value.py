# %%
from enum import Enum


class AIModel(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


model = AIModel("alexnet")
assert model.value == "alexnet"
