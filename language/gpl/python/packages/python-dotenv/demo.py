# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv>=1.2.1",
# ]
# ///
import os

from dotenv import load_dotenv

load_dotenv()
secret = os.getenv("SECRET_KEY")
print(secret)
