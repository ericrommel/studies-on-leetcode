"""
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the
elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
from operator import length_hint

import pytest
from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length

        prefix = 1
        for i in range(length):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(length - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result


@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize(
    'nums, expected',
    [
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
        ([2, 3, 4, 5], [60, 40, 30, 24]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
    ]
)
def test_product_except_self(nums, expected, solution):
    assert solution.product_except_self(nums) == expected
