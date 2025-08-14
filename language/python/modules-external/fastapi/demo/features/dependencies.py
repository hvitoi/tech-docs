from typing import Annotated
from fastapi import APIRouter, Cookie, Depends, HTTPException, Header, Query


router = APIRouter(
    prefix="/dependencies",
    tags=["Dependencies"],
)


## --- Common Parameters (with dependency function)
# The parameters come from the request input (Query, Path, Body, etc)
async def get_common_parameters(
    limit: Annotated[int, Query()] = 1000,
    skip: Annotated[int, Query()] = 0,
):
    return {"limit": limit, "skip": skip}


@router.get("/deps1")
def demo_dependencies(
    common_parameters: Annotated[dict, Depends(get_common_parameters)],
):
    limit = common_parameters["limit"]
    skip = common_parameters["skip"]
    print(limit, skip)
    return None


## --- Common Parameters (with dependency class)


class CommonParameters:
    def __init__(
        self,
        limit: Annotated[int, Query()] = 1000,
        skip: Annotated[int, Query()] = 0,
    ):
        self.limit = limit
        self.skip = skip


@router.get("/deps2")
def demo_dependencies2(
    # common_parameters: Annotated[CommonParameters, Depends(CommonParameters)], # verbose way
    common_parameters: Annotated[CommonParameters, Depends()],  # it knows the class
):
    print(common_parameters.limit, common_parameters.skip)
    return None


## --- Database connection
class DBSession:
    def __init__(self):
        print("Starting connection")
        self.status = "connected"

    def close(self):
        print("Closing DB connection")


def get_db():
    db = DBSession()
    # dependable functions always finish the close execution when using yield
    # That means that FastAPI injects that value, waits for your endpoint to finish, and then runs whatever code comes after the yield (calling next())
    try:
        yield db
    finally:
        # Teardown Logic
        db.close()


# class DBSessionContextManager:
#     def __init__(self):
#         self.db = DBSession()

#     def __enter__(self):
#         return self.db

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.db.close()

# def get_db():
#     with DBSessionContextManager() as db:
#         yield db


@router.get("/deps3")
def dependable_class(db: Annotated[DBSession, Depends(get_db)]):
    return {"db_status": db.connection_status}


## --- Sub-dependencies
# If one of your dependencies is declared multiple times for the same
# path operation, for example, multiple dependencies have a
# common sub-dependency, FastAPI will know to call that sub-dependency
# only once per request. It will be cached once and used for all the uses in that request flow
# You can change this behavior with Depends(get_value, use_cache=False)


class AlphaParam:
    def __init__(self, alpha_param: Annotated[str, Query()]):
        self.alpha_param = alpha_param


class BetaParam:
    def __init__(self, beta_param: Annotated[str, Query()]):
        self.beta_param = beta_param


# Dependable (for the path operation function) and Dependent (fot the AlphaParam and BetaParm classes)
class AlphaBetaParams:
    def __init__(
        self,
        a: Annotated[AlphaParam, Depends()],
        b: Annotated[BetaParam, Depends()],
    ):
        self.alpha_param = a.alpha_param
        self.beta_param = b.beta_param


@router.get("/deps4")
async def deps4(
    params: Annotated[AlphaBetaParams, Depends()],
):
    return {
        "alpha_param": params.alpha_param,
        "beta_param": params.beta_param,
    }


## --- Dependencies as path decorators
# This is used when the return value of that dependency is not important


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key  # The value is returned here but never used


@router.get(
    "/deps5",
    dependencies=[  # Dependencies could also be added at the global level FastAPI()
        Depends(verify_token),
        Depends(verify_key),
    ],
)
async def verify_tokens():
    return "you are allowed"
