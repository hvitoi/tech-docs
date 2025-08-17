from typing import Annotated, Literal
from fastapi import APIRouter, Query
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/queryparams",
    tags=["Input Query Parameters"],
)

# Query parameters are request parameters whose type is annotated with "Query()"
# Or it can be inferred: it's not a path variable (path parameter) and is not associated with a Pydantic Model (request body)


@router.get("/foo")
def read_items(
    q1: str,
    q2: bool,  # ... bool accepts True, true, 1, on, yes
    q3: Annotated[
        str | None,
        Query(
            title="My awesome querystring",
            description="This is used to...",
            alias="my-q1",  # the querystring can be passed as this name too, useful for using "-" character
            min_length=3,  # validation
            max_length=50,  # validation
            pattern="^fixedquery$",  # validation
            deprecated=True,  # show in as deprecated in docs
            include_in_schema=True,  # Change it to false to hide it from the OpenAPI schema
            # in order to use custom validators, check pydantic.AfterValidator (not for validation with external data though)
        ),
    ] = None,
    q4: Annotated[
        list[str], Query()
    ] = [],  # ?q2=foo&q2=bar ; this needs the Query() annotation otherwise it would be confused with a Request Body
):
    return {
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "q4": q4,
    }


## ---
# Declare all the query parameters as a single Pydantic model
# The validations are then defined in the Pydantic model for each querystring


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)  # Sets the validation rules
    order_by: Literal["created", "updated_at"] = "created_at"  # Sets the default value
    tags: list[str] = []

    # "model_config" is a special parameter. You can define, for example, if the user is not allowed to pass querstrings not defined here
    model_config = {"extra": "forbid"}


@router.get("/items/")
def read_items2(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
