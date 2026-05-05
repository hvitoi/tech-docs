# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests>=2.32.5",
# ]
# ///
import requests

print(requests.get("http://example.com"))

# To add the dependency to the header of the file
# --> uv add requests --script demo.py

# To run the file with the dependencies
# --> uv run demo.py
