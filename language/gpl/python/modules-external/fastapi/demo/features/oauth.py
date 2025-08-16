from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel


router = APIRouter(
    prefix="/oauth",
    tags=["OAuth"],
)

# What this Dependency does is:
#  - Document (via OpenAPI) that this API uses OAuth 2.0's "password" grant type
#  - Validate that a Bearer token is received and return it to the path operation function
#  - If the Bearer token is not provided then returns 401 (unauthorized) directly

oauth2_scheme = OAuth2PasswordBearer(
    # This is the authorization server
    # tokenUrl="https://authorization-server.com/oauth2/token"
    tokenUrl="/oauth/token"  # /oauth is the prefix of the router
)

fake_users_db = {
    "henry": {
        "username": "henry",
        "full_name": "Henry Vitoi",
        "email": "henry@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "henka": {
        "username": "henka",
        "full_name": "Henka Vitoinen",
        "email": "henka@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": True,
    },
}


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserDB(User):
    hashed_password: str


def get_user(token: str):
    username = token  # decode the token and get the username
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return UserDB(**user_dict)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = get_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={
                "WWW-Authenticate": "Bearer"  # This header is always responded in the OAuth2 spec whenever an auth problem has occurred with the bearer token
            },
        )
    if user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


@router.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserDB(**user_dict)
    hashed_password = "fakehashed" + form_data.password
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {
        "access_token": user.username,
        "token_type": "bearer",
    }
