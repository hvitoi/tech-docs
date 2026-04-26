# %%

# Every Python module has a __name__ variable.
# - If the file is run directly (e.g., python app.py), __name__ is set to "__main__".
# - If the file is imported as a module from another file, __name__ is set to the module's name (e.g., "app").

print(__name__)  # __main__


# %%
# This idiom is a safe way to make a Python file runnable and importable without side effects.
if __name__ == "__main__":
    print("I was run directly. I was not imported by other module.")
