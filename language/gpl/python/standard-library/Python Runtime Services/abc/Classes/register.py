# %%
# ABC.register(cls) -- declare `cls` to be a "virtual subclass" of an ABC,
# WITHOUT real inheritance. Affects isinstance / issubclass only.
#
# Use case: you want third-party or built-in types to be recognized as your ABC
# without modifying their source.

from abc import ABC, abstractmethod


class JSONLike(ABC):
    @abstractmethod
    def to_json(self): ...


class TupleAdapter:
    def to_json(self):
        return "[...]"


JSONLike.register(TupleAdapter)

isinstance(TupleAdapter(), JSONLike)  # True
issubclass(TupleAdapter, JSONLike)  # True

# %%
# Caveat 1: registration does NOT enforce abstract methods.
# A virtual subclass can lack to_json entirely and Python won't complain.


class Broken:
    pass


JSONLike.register(Broken)
isinstance(
    Broken(), JSONLike
)  # True (!) -- but Broken().to_json() would AttributeError

# %%
# Caveat 2: virtual subclasses don't inherit anything. No methods, no attributes.
# It's a *claim* about type identity, not real subclassing.


# %%
# Can be used as a decorator
@JSONLike.register
class DictAdapter:
    def to_json(self):
        return "{...}"


# %%
# This is how `collections.abc` makes built-ins like list/tuple/dict/str
# count as Iterable, Sized, Container, etc. -- via __subclasshook__,
# which is the structural-typing version of register().

from collections.abc import Sized


class HasLen:
    def __len__(self):
        return 0


# No registration needed -- Sized.__subclasshook__ accepts anything with __len__
issubclass(HasLen, Sized)  # True
