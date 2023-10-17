"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation:
  After squaring, the array becomes [16,1,0,9,100].
  After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 10**4
-10**4 <= nums[i] <= 10**4
nums is sorted in non-decreasing order.
"""
import big_o
import pytest


class Solution:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        squares = [i*i for i in nums]
        squares.sort()
        return squares


@pytest.mark.parametrize("test_input, expected", [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
])
def test_sorted_squares(test_input, expected):
    assert Solution().sorted_squares(nums=test_input) == expected


def test_complexity(capsys):
    with capsys.disabled():
        # Generating random test data of length 100
        test_data = lambda n: big_o.datagen.integers(n, -10 ** 4, 10 ** 4)

        # Calculating the Time complexity
        best, others = big_o.big_o(Solution().sorted_squares, test_data, n_measures=100)
        print(f"\n{big_o.reports.big_o_report(best, others)}")
