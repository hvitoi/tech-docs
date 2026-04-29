# %%
import asyncio


def merge_sort(col: list[int]) -> list[int]:
    """O(n log n) time; O(n) space; stable
    The recursive calls share no state, they can run in different threads or machines
    The merging of the two sorted collections need to be synchronized in the same machine
    This a classic fork-join or map-reduce problem
    """
    if len(col) <= 1:
        return col

    mid = len(col) // 2
    left = merge_sort(col[:mid])
    right = merge_sort(col[mid:])
    return _merge_sorted_cols(left, right)


async def merge_sort_async(col: list[int]) -> list[int]:
    """Naive solution for concurrently sorting. Asyncio is I/O bound, and partitioning is purely CPU bound"""
    if len(col) <= 1:
        return col

    mid = len(col) // 2
    # asyncio.gather schedules concurrently — but neither task ever awaits I/O,
    # so they run sequentially on the same thread anyway.
    left, right = await asyncio.gather(
        merge_sort_async(col[:mid]),
        merge_sort_async(col[mid:]),
    )
    return _merge_sorted_cols(left, right)


def _merge_sorted_cols(left: list[int], right: list[int]) -> list[int]:
    """
    O(n + m) time; O(n + m) space
    This is a "two pointers" algorithm pattern
    This algorithm related the problems:
        - "merge-sorted-array" (with arrays)
        - "merge-two-sorted-lists" (with linked lists, so a difference implementations)
        - "merge-k-sorted-lists": same idea, but solved with a heap instead
    """
    merged: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])  # drain the rest
    merged.extend(right[j:])  # drain the rest
    return merged


assert merge_sort([4, 5, 1, 3, 2]) == [1, 2, 3, 4, 5]
assert merge_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert merge_sort([2, 1, 2, 1, 2]) == [1, 1, 2, 2, 2]
assert merge_sort([]) == []
assert merge_sort([1]) == [1]
assert merge_sort([1, 1]) == [1, 1]
