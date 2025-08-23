# %%
from random import randint
from unittest.mock import Mock

# A Mock is a fake callable you can use in place of a real one.

any_function = Mock(return_value="foo")
any_function()  # foo
randint = Mock(return_value=0.500)
randint()  # replace completely the randint function
randint(1, 2, 3, 4)  # doesn't matter the arity
