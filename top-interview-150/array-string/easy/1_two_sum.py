"""
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
import pytest
from typing import List


class Solution:
    # O(n^2)
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # O(n)
    def two_sum_2(self, nums: List[int], target: int) -> List[int]:
        num_map = {} # number as key, index as value
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize(
    'nums, target, expected',
    [
        ([2,5,5,11], 10, [1, 2]),
        ([2,7,11,15], 9, [0,1]),
        ([3,2,4], 6, [1,2]),
        ([3,3], 6, [0, 1]),
    ]
)
def test_two_sum(nums, target, expected, solution):
    assert solution.two_sum(nums, target) == expected


@pytest.mark.parametrize(
    'nums, target, expected',
    [
        ([2,5,5,11], 10, [1, 2]),
        ([2,7,11,15], 9, [0,1]),
        ([3,2,4], 6, [1,2]),
        ([3,3], 6, [0, 1]),
    ]
)
def test_two_sum_2(nums, target, expected, solution):
    assert solution.two_sum_2(nums, target) == expected
