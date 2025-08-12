from enum import Enum
from fastapi import APIRouter

router = APIRouter(
    # prefix="/foo",
    tags=["Path Parameters"],
)

# Path parameters are the parameter whose type is annotated with Path()
# Or it can be inferred: its variable name is contained in the path


class AIModel(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@router.get("/models/{model_name}")
def read_model(model_name: AIModel):  # Enum
    if model_name is AIModel.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
