# %%
import inspect


def greet(name: str):
    """This function greets the user"""
    return f"Hello {name}"


inspect.getdoc(greet)
