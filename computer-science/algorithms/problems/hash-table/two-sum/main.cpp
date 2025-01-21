#include <cassert>
#include <unordered_map>
#include <vector>

// Brute force solution
std::vector<int> two_sum_brute_force(const std::vector<int> &nums,
                                     const int target) {
  int n = nums.size();

  for (int i = 0; i < n; i++) {
    // for (int j = 0; j < n; j++) {
    for (int j = i + 1; j < n; j++) {
      if (i == j) {
        continue;
      }
      if ((nums[i] + nums[j]) == target) {
        return {i, j};
      }
    }
  }

  return {};
}

std::vector<int> two_sum_has_been_seen(const std::vector<int> &nums,
                                       const int target) {
  std::unordered_map<int, int> seen; // value, index

  int n = nums.size();
  for (int i = 0; i < n; i++) {
    int complement = target - nums[i];
    if (seen.count(complement)) {
      return {seen[complement], i};
    }
    seen[nums[i]] = i;
  };

  return {};
}

int main() {
  {
    auto actual = two_sum_brute_force({2, 7, 11, 15}, 9);
    std::vector<int> expected{0, 1};
    assert(expected == actual);

    auto actual2 = two_sum_has_been_seen({2, 7, 11, 15}, 9);
    std::vector<int> expected2{0, 1};
    assert(expected2 == actual2);
  }

  {
    auto actual = two_sum_brute_force({3, 2, 4}, 6);
    std::vector<int> expected{1, 2};
    assert(expected == actual);
  }

  {
    auto actual = two_sum_brute_force({3, 3}, 6);
    std::vector<int> expected{0, 1};
    assert(expected == actual);
  }

  return 0;
}
