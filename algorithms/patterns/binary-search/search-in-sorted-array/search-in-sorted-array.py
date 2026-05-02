# %%


def binary_search(arr: list[int], target: int) -> bool:
    """O(log n)"""
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if target == arr[mid]:
            return True

        if target < arr[mid]:
            hi = mid - 1
            continue

        if target > arr[mid]:
            lo = mid + 1
            continue

    return False


def binary_search_recursive(arr: list[int], target: int):
    """O(log n)"""

    def bs(lo: int, hi: int):
        if (hi - lo) < 0:
            return False

        mid = lo + (hi - lo) // 2

        if target == arr[mid]:
            return True

        if target < arr[mid]:
            return bs(lo, mid - 1)

        if target > arr[mid]:
            return bs(mid + 1, hi)

    return bs(0, len(arr) - 1)


for fn in [binary_search, binary_search_recursive]:
    assert fn([1, 2, 3, 4, 5], 4) is True
    assert fn([1, 2, 3, 4, 5], 99) is False
    assert fn([], 99) is False
