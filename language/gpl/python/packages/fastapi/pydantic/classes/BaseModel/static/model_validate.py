# %%
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime = datetime.now()
    friends: list[int] = []


# Return the user created if the validation is passed
User.model_validate({"id": "123", "name": "Henry"})

# Throws
User.model_validate({"id": "123"})  # name is required
