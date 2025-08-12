from enum import Enum
from fastapi import APIRouter

router = APIRouter(
    # prefix="/foo",
    tags=["Path Parameters"],
)


class AIModel(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# Path parameters also automatically inferred when its variable name is container in the path


@router.get("/models/{model_name}")
def read_model(model_name: AIModel):  # Enum
    if model_name is AIModel.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
