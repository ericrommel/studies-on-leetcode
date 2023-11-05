"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation:
    9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation:
    2 does not exist in nums so return -1

Constraints:
1 <= nums.length <= 10**4
-10**4 < nums[i], target < 10**4
All the integers in nums are unique.
nums is sorted in ascending order.
"""
import random
from time import sleep

import big_o
import pytest


class Solution:
    '''
    This is the Template #1 and it is used to search for an element or condition which can be determined by accessing
    a single index in the array.
    - Most basic and elementary form of Binary Search
    - Search Condition can be determined without comparing to the element's neighbors or use specific elements around it
    - No post-processing required because at each step, you are checking to see if the element has been found. If you
      reach the end, then you know the element is not found
    '''
    def search(self, nums: list[int], target: int) -> int:
        # Special case
        if len(nums) == 0:
            return -1

        # Init start and end positions
        left, right = 0, len(nums) - 1

        # Search
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1  # Searching Right side
            else:
                right = mid - 1  # Searching Left side

        return -1


@pytest.mark.parametrize("test_input, test_target, expected", [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
])
def test_search(test_input, test_target, expected):
    assert Solution().search(nums=test_input, target=test_target) == expected


# The lib Big-O currently doesn't support more than 1 parameter to check. This is a workaround but measures can be wrong
def aux_function(arr):
    # Select one of the targets in the array
    target_idx = random.randint(0, len(arr))
    target = arr[target_idx]
    return Solution().search(nums=arr, target=target)


def test_complexity(capsys):
    with capsys.disabled():
        test_data = lambda n: sorted(big_o.datagen.integers(n*100, 1, 10**8))  # binary search expects the list to be sorted

        # Calculating the Time complexity
        best, others = big_o.big_o(aux_function, test_data, n_measures=10, n_repeats=10, return_raw_data=True)
        print(f"\n{big_o.reports.big_o_report(best, others)}")
