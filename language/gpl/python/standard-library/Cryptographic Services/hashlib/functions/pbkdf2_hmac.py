# %%

import os
import hashlib
import binascii


def hash_password(password: str) -> str:
    # Generate a random 16-byte salt
    salt = os.urandom(16)

    # Derive a secure hash using PBKDF2-HMAC-SHA256
    key = hashlib.pbkdf2_hmac(
        "sha256",  # Hash algorithm
        password.encode("utf-8"),  # Convert password to bytes
        salt,  # Salt
        100_000,  # Iterations (increase for more security)
    )

    # Store salt and key together (hex-encoded) for later verification
    return binascii.hexlify(salt + key).decode("utf-8")


def verify_password(stored_hash: str, password: str) -> bool:
    data = binascii.unhexlify(stored_hash.encode("utf-8"))
    salt = data[:16]  # First 16 bytes = salt
    key = data[16:]  # Rest = hash
    new_key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
    return key == new_key


hashed = hash_password("my_secret_password")
print("Stored hash:", hashed)
print("Verify OK:", verify_password(hashed, "my_secret_password"))
print("Verify FAIL:", verify_password(hashed, "wrong_password"))
