# %%
from passlib.context import CryptContext

# password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
PASSWORD = "secret"

# ----

hashed_password = pwd_context.hash(PASSWORD)
print(hashed_password)

is_password_verified = pwd_context.verify("secret", hashed_password)
print(is_password_verified)
