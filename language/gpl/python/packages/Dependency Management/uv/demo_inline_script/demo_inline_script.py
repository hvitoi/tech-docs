# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "requests>=2.32.5",
# ]
# ///

import requests


def main() -> None:
    print(requests.get("http://example.com"))


if __name__ == "__main__":
    main()


# To add the dependency to the header of the file
# --> uv add requests --script demo.py

# To run the file with the dependencies
# --> uv run demo.py
