# %%
from datetime import datetime, time, timedelta
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, HttpUrl, SecretStr


class User(BaseModel):
    id: UUID
    name: str
    signup_ts: datetime = datetime.now()  # default value
    process_after: timedelta | None = None  # optional field
    repeat_at: time | None = None  # optional field
    friends: list[int] = []  # default value
    url: HttpUrl
    email: EmailStr
    my_secret: SecretStr | None = None

    # The "Field" allows passing more validation and metadata
    description: str | None = Field(  # Field accepts the same args as Body()
        default=None,  # default values are passed like this when Field validations are necessary
        title="The description of the user",
        max_length=300,
        examples=["It's a handsome boy"],
    )
    limit: int = Field(
        100,  # default value
        gt=0,
        le=100,
    )
    favorite_number: int = Field(
        default_factory=int,  # 0 by default
    )


data = {
    "id": "8be4df61-93ca-11d2-aa0d-00e098032b8c",
    "name": "Henry",
    "url": "https://example.com",
    "email": "foo@bar.com",
}

# Deserializes the data, throws if it's invalid!
User(**data)
