# %%
my_list = []

def modify_list() -> None:
    my_list.append("a")  # works! (in-place modification)

def modify_list2(ls: list) -> None:
    ls.append("b")  # works! (in-place modification)

def modify_list3(ls: list) -> None:
    ls[:] = ls + ["c"]  # works! (in-place modification)

def try_to_modify_list(ls: list) -> None:
    ls = ["z"]  # does not work! Reassigns only the local pointer


modify_list()
modify_list2(my_list)
modify_list3(my_list)
try_to_modify_list(my_list)
my_list


# %%
# Prevent side effects
import copy

arr = ["a", "b", "c"]

def fn_without_side_effects(arr: list) -> list:
    arr = copy.deepcopy(arr)
    arr.append("z")
    return arr

fn_without_side_effects(arr)
arr  # original array untouched
