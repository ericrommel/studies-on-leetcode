"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

*Note* that elements beyond the length of the original array are not written. Do the above modifications to the input
       array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation:
  After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation:
  After calling your function, the input array is modified to: [1,2,3]


Constraints:
1 <= arr.length <= 10**4
0 <= arr[i] <= 9
"""
import copy

import big_o
import pytest


class Solution:
    def duplicate_zeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0
        for _ in range(len(arr)):
            if idx >= len(arr):
                break
            if arr[idx] == 0:
                arr.insert(idx + 1, 0)
                arr.pop()
                idx += 1
            idx += 1

    def duplicate_zeros_2(self, arr: list[int]) -> None:
        for i in range(len(arr) - 1, -1, -1):
            if not arr[i]:
                arr.insert(i, 0)
                arr.pop()


@pytest.mark.parametrize("test_input, expected", [
    ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
    ([1, 2, 3], [1, 2, 3]),
])
def test_duplicate_zeros(test_input, expected):
    Solution().duplicate_zeros(arr=test_input)
    assert test_input == expected


@pytest.mark.parametrize("test_input, expected", [
    ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
    ([1, 2, 3], [1, 2, 3]),
])
def test_duplicate_zeros_2(test_input, expected):
    Solution().duplicate_zeros_2(arr=test_input)
    assert test_input == expected
