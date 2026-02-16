# %%
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime = datetime.now()
    friends: list[int] = []


data = {"id": "123", "name": "Henry"}
User(**data)
