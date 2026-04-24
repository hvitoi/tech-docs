# %%
# another option is just to pick a number and then apply 2sum, in this case the time complexity would be O(n^2)

from unittest import TestCase


def three_sum_brute_force(nums: list[int]) -> list[list[int]]:
    triplets = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i:
                continue
            for k in range(len(nums)):
                if k == j or k == i:
                    continue
                triplet = tuple(sorted((nums[i], nums[j], nums[k])))
                if sum(triplet) == 0:
                    triplets.add(triplet)
    return list(sorted(map(list, triplets)))


def three_sum_brute_force_recursion(nums: list[int], k=3) -> list[list[int]]:
    """
    Choice: pick an element at each recursion stack and then pass the remaining elements forward
    """

    def kplets(nums, k) -> set[tuple]:
        if k == 0:
            return {()}

        acc = set()

        for i in range(len(nums)):
            remaining_nums = nums[:i] + nums[i + 1 :]
            options = kplets(remaining_nums, k - 1)
            combinations = [tuple(sorted((nums[i],) + option)) for option in options]
            acc.update(combinations)

        return acc

    return list(
        sorted(map(list, filter(lambda kplet: sum(kplet) == 0, kplets(nums, 3))))
    )


test_case = TestCase()

for fn in {three_sum_brute_force, three_sum_brute_force_recursion}:
    test_case.assertEqual(fn([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
    test_case.assertEqual(fn([0, 1, 1]), [])
    test_case.assertEqual(fn([0, 0, 0]), [[0, 0, 0]])
