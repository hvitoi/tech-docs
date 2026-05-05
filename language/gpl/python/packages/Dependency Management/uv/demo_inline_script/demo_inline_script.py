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
