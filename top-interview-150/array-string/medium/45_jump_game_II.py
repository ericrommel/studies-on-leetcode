"""
You are given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at nums[0].
Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at
`nums[i]`, you can jump to any `nums[i + j]` where:

- 0 <= j <= nums[i] and
- i + j < n

Return the minimum number of jumps to reach `nums[n - 1]`. The test cases are generated such that you can reach
`nums[n - 1]`.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""
import pytest
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 # no jumps are needed

        jumps = 0 # To count the minimal jumps
        max_reach = 0 # The farthest we can reach with the current jump
        current_end = 0 # the farthest we can go with the current set of jumps

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == current_end: # reached the end of the current jump range?
                jumps += 1 # jump
                current_end = max_reach
                if current_end >= len(nums) - 1: # reach the last index?
                    break

        return jumps


@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize(
    "nums, expected",
    [
        # ([2,3,1,1,4], 2),
        # ([2,3,0,1,4], 2),
        ([0], 0),
        ([1], 0)
    ]
)
def test_jump(nums, expected, solution):
    assert solution.jump(nums) == expected
