"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 10**5
nums[i] is either 0 or 1.
"""
import big_o.datagen
import pytest


class Solution:

    def find_max_consecutive_ones(self, nums: list[int]) -> int:
        max_count = 0
        ctrl = 0
        for i in nums:
            if i == 1:
                ctrl += 1
                max_count = max(ctrl, max_count)
            else:
                ctrl = 0
        return max_count


@pytest.mark.parametrize("test_input, expected", [
    ([1, 1, 0, 1, 1, 1], 3),
    ([1, 0, 1, 1, 0, 1], 2),
    ([1, 1, 1, 1, 1, 1], 6),
    ([0, 0, 0, 0, 0, 0], 0),
    ([0, 0, 0, 0, 0, 1], 1),
    ([1, 0, 0, 0, 0, 0], 1),
])
def test_find_max_consecutive_ones(test_input, expected):
    assert Solution().find_max_consecutive_ones(nums=test_input) == expected


def test_complexity(capsys):
    with capsys.disabled():
        test_data = lambda n: big_o.datagen.integers(n, 0, 1)

        # Calculating the Time complexity
        best, others = big_o.big_o(Solution().find_max_consecutive_ones, test_data, n_measures=100)
        print(f"\n{big_o.reports.big_o_report(best, others)}")
