# %%
from functools import partial


def do_something(fn):
    for el in range(10):
        fn(el)


my_list = []
append_to_list = partial(lambda ls, el: ls.append(el), my_list)
do_something(append_to_list)
my_list
