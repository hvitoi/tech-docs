# %%
import jwt

jwt_str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30"
SECRET_KEY = "a-string-secret-at-least-256-bits-long"  # "openssl rand -hex 16" to get a secret key
SIGNING_ALGORITHM = "HS256"

payload = {
    "sub": "1234567890",
    "name": "Henry Vitoi",
    "admin": True,
}

# Generate jwt with the given payload
# The headers {"alg": "HS256","typ": "JWT"} are automatically added to the jwt
jwt_str = jwt.encode(payload, SECRET_KEY, algorithm=SIGNING_ALGORITHM)
print(jwt_str)

# Get the payload only (no headers). And throws if it fails de verification
payload_decoded = jwt.decode(jwt_str, SECRET_KEY, algorithms=[SIGNING_ALGORITHM])
print(payload_decoded)
