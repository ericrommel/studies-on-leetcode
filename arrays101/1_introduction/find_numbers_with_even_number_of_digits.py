"""
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
 12 contains 2 digits (even number of digits).
 345 contains 3 digits (odd number of digits).
 2 contains 1 digit (odd number of digits).
 6 contains 1 digit (odd number of digits).
 7896 contains 4 digits (even number of digits).
 Therefore only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555,901,482,1771]
Output: 1
Explanation:
 Only 1771 contains an even number of digits.


Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10**5
"""
import big_o
import pytest


class Solution:
    def find_numbers(self, nums: list[int]) -> int:
        count_even = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count_even += 1
        return count_even

    def find_numbers_faster(self, nums: list[int]) -> int:
        return len([i for i in nums if len(str(i)) % 2 == 0])


@pytest.mark.parametrize("test_input, expected", [
    ([12, 345, 2, 6, 7896], 2),
    ([555, 901, 482, 1771], 1),
])
def test_find_numbers(test_input, expected):
    assert Solution().find_numbers(nums=test_input) == expected


def test_complexity(capsys):
    with capsys.disabled():
        test_data = lambda n: big_o.datagen.integers(n, 1, 10**5)

        # Calculating the Time complexity
        best, others = big_o.big_o(Solution().find_numbers, test_data, n_measures=100)
        print(f"\n{big_o.reports.big_o_report(best, others)}")

        best, others = big_o.big_o(Solution().find_numbers_faster, test_data, n_measures=100)
        print(f"\n{big_o.reports.big_o_report(best, others)}")
