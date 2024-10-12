"""
Given an array `nums` of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
import pytest
from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3,2,3], 3),
        ([2,2,1,1,1,2,2], 2)
    ]
)
def test_solution(nums, expected, solution):
    assert solution.majority_element(nums) == expected