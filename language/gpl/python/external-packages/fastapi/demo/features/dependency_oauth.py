from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from pydantic import BaseModel
from passlib.context import CryptContext


router = APIRouter(
    prefix="/oauth",
    tags=["OAuth"],
)

## ---- Signing configuration

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SIGNING_SECRET_KEY = "a-string-secret-at-least-256-bits-long"  # "openssl rand -hex 16" to get a secret key
SIGNING_ALGORITHM = "HS256"  # HMAC with SHA-256: it's a symmetric algorithm! (less secure in multi-party or public scenarios)
ACCESS_TOKEN_EXPIRE_MINUTES = 30


## ---- Common functions

fake_users_db = {
    "henry": {
        "username": "henry",
        "full_name": "Henry Vitoi",
        "email": "henry@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # hashed representation of "secret"
        "disabled": False,
    },
    "henka": {
        "username": "henka",
        "full_name": "Henka Vitoinen",
        "email": "henka@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": True,
    },
}


def get_user(db, username):
    if username in db:
        return UserDB(**db[username])


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserDB(User):
    hashed_password: str


## ---- Authorization Server


class Token(BaseModel):
    access_token: str
    token_type: str


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(fake_db, username: str, password: str) -> User | None:
    user = get_user(fake_db, username)
    if (not user) or (not verify_password(password, user.hashed_password)):
        return
    return user


def create_jwt(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expires_at = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expires_at})
    encoded_jwt = jwt.encode(
        to_encode,  # payload (the data to include inside the JWT) - not the headers!
        SIGNING_SECRET_KEY,  # key used to sign the JWT (private key for asymmetric, or shared secret for HMAC)
        algorithm=SIGNING_ALGORITHM,  # signing algorithm (e.g. HS256, RS256, ES256)
    )
    return encoded_jwt


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_jwt(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )
    return Token(
        access_token=access_token,
        token_type="bearer",
    )


## ---- Resource Server


# What this Dependency does is:
#  - Document (via OpenAPI) that this API uses OAuth 2.0's "password" grant type
#  - Validate that a Bearer token is received and return it to the path operation function
#  - If the Bearer token is not provided then returns 401 (unauthorized) directly

oauth2_scheme = OAuth2PasswordBearer(
    # This is the authorization server
    # tokenUrl="https://authorization-server.com/oauth2/token"
    tokenUrl="/oauth/token"  # /oauth is the prefix of the router
)


class JwtContent(BaseModel):
    username: str | None = None


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer"  # This header is always responded in the OAuth2 spec whenever an auth problem has occurred with the bearer token
        },
    )

    try:
        payload = jwt.decode(token, SIGNING_SECRET_KEY, algorithms=[SIGNING_ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = JwtContent(username=username)

    except jwt.InvalidTokenError:
        raise credentials_exception

    # at that point the jwt is authentic
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception

    return user


@router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user
