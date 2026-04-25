# https://leetcode.com/problems/3sum/ - 35k likes (Apr/2026)
# %%
# another option is just to pick a number and then apply 2sum, in this case the time complexity would be O(n^2)


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


def three_sum(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                incumbent = sorted([nums[i], nums[j], nums[k]])
                if sum(incumbent) == 0 and incumbent not in result:
                    result.append(incumbent)
    return sorted(result)


for fn in {three_sum_brute_force, three_sum_brute_force_recursion, three_sum}:
    assert fn([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert fn([0, 1, 1]) == []
    assert fn([0, 0, 0]) == [[0, 0, 0]]
