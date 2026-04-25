# %%
from typing import Annotated
# Type Hints with Metadata Annotations


def say_hello(name: Annotated[str, "the name of whom you will say hello to"]) -> str:
    return f"Hello {name}"
