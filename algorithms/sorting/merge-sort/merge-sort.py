# %%
import asyncio
import inspect
import os
from concurrent.futures import ThreadPoolExecutor


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
    return merge_sorted(left, right)


async def merge_sort_parallel_asyncio(col: list[int]) -> list[int]:
    """Naive solution for concurrently sorting. Asyncio is I/O bound, and partitioning is purely CPU bound"""
    if len(col) <= 1:
        return col

    mid = len(col) // 2
    # asyncio.gather schedules concurrently — but neither task ever awaits I/O,
    # so they run sequentially on the same thread anyway.
    left, right = await asyncio.gather(
        merge_sort_parallel_asyncio(col[:mid]),
        merge_sort_parallel_asyncio(col[mid:]),
    )
    return merge_sorted(left, right)


def merge_sort_parallel_threads(col: list[int]) -> list[int]:
    """Parallel execution with the GIL removal (Python 3.13+ built with --disable-gil)

    We fork only down to a depth that saturates available cores; deeper recursion
    stays sequential to avoid thread-scheduling overhead dominating the work.
    """

    def _merge_sort_parallel_threads(col: list[int], depth: int) -> list[int]:
        if depth == 0:
            return merge_sort(col)

        mid = len(col) // 2

        # execute left in a new thread
        left = executor.submit(_merge_sort_parallel_threads, col[:mid], depth - 1)

        # execute right in the same thread
        right = _merge_sort_parallel_threads(col[mid:], depth - 1)

        # merge results
        return merge_sorted(left.result(), right)

    workers = os.cpu_count() or 1
    max_depth = (workers - 1).bit_length()  # ceil(log2(workers))

    with ThreadPoolExecutor(max_workers=workers) as executor:
        return _merge_sort_parallel_threads(col, max_depth)


# ----


def merge_sorted(left: list[int], right: list[int]) -> list[int]:
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


for fn in [merge_sort, merge_sort_parallel_asyncio, merge_sort_parallel_threads]:
    run = (
        (lambda *args, **kwargs: asyncio.run(fn(*args, **kwargs)))  # for coroutines
        if inspect.iscoroutinefunction(fn)
        else fn  # for conventional functions (includes the one with threads)
    )

    assert run([4, 5, 1, 3, 2]) == [1, 2, 3, 4, 5]
    assert run([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert run([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert run([2, 1, 2, 1, 2]) == [1, 1, 2, 2, 2]
    assert run([]) == []
    assert run([1]) == [1]
    assert run([1, 1]) == [1, 1]
    assert run(list(range(1000, 0, -1))) == list(range(1, 1001))
