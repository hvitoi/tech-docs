# Type Hints (Type annotations)

- Type Hints or annotations are a special syntax that allow declaring the type of a variable.

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
