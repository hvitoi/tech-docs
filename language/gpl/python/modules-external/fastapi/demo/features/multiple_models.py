from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(
    prefix="/multiplemodels",
    tags=["Multiple Models"],
)


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserDB(UserBase):
    hashed_password: str


def save_user(user_in: UserIn):
    hashed_password = "simulehashing" + user_in.password
    user_in_db = UserDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! (fake)")
    return user_in_db


@router.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = save_user(user_in)
    return user_saved
