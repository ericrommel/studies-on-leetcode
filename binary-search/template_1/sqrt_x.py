"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer
should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation:
    The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation:
    The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:
0 <= x <= 2**31 - 1
"""
import pytest


class Solution:
    def my_sqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left, right = 0, x//2 + 1
        mid, check_mult = 0, 0
        while left <= right:
            mid = (left + right) // 2
            check_mult = mid * mid
            if check_mult == x:
                return mid
            elif check_mult < x:
                left = mid + 1
            else:
                right = mid - 1
        return mid if check_mult < x else right


@pytest.mark.parametrize("test_input, expected", [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (8, 2),
    (36, 6),
    (2147395599, 46339)
])
def test_my_sqrt(test_input, expected):
    assert Solution().my_sqrt(x=test_input) == expected
