# Type Hints (Type annotations)

- Python is `dynamically typed` (contrary to C++, Java, etc that are statically typed). With python you can provide `type hints` to assist on the development
- `Type Hints` or `Annotations` are a special syntax that allow declaring the type of a variable
- Type hints are not validated at runtime! That means that even if you provide wrong types it will compile normally

> Python will remain a dynamically typed language, and the authors have no desire to ever make type hints mandatory, even by convention.

```python
type SetOfIntegers = set[int]

a: SetOfIntegers = {1, 2, 3}
b: set[int] = {1, 2, 3}
```

## Classes as types

```python
class Person:
    def __init__(self, name: str):
        self.name = name


person: Person = Person("Henry")
```

- Types are usually represented in form of `classes`

## Generic Types

- Types that take parameters. Example: `dict[str, int]`
