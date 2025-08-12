from typing import Annotated
from fastapi import APIRouter, Query

router = APIRouter(
    tags=["Query Parameters"],
)

# Query string are parameters whose type is annotated with "Query()"
# Or it can also be inferred, that is: it's not a path variable (path parameter) and is not associated with a Pydantic Model (reques body)


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
