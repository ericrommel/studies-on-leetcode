"""
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Follow up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
import pytest
from typing import List

class Solution:
    # Using Slicing: Time: O(n), Space: O(n)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    # Using Reversal Algorithm: Time: O(n), Space: O(1)
    def rotate_2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        # Step 1: Reverse the entire list
        self.reverse_in_place(nums, 0, n-1)

        # Step 2: Reverse the first k elements
        self.reverse_in_place(nums, 0, k-1)

        # Step 3: Reverse the remaining n-k elements
        self.reverse_in_place(nums, k, n-1)

    def reverse_in_place(self, nums: List[int], start: int, end: int) -> List[int]:
        half = (end - start + 1) // 2
        for i in range(half):
            nums[start + i], nums[end - i] = nums[end - i], nums[start + i]
        return nums


    def rotate_3(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        count = 0
        start = 0

        while count < n:
            current = start
            prev = nums[start]

            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                # If we return to the starting point, break the cycle
                if start == current:
                    break

            start += 1


@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize(
    "nums, rotation, expected",
    [
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
        ([-1,-100,3,99], 2, [3,99,-1,-100]),
    ]
)
def test_rotate(nums, rotation, expected, solution):
    solution.rotate(nums, rotation)
    assert nums == expected

@pytest.mark.parametrize(
    "nums, rotation, expected",
    [
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
        ([-1,-100,3,99], 2, [3,99,-1,-100]),
    ]
)
def test_rotate_2(nums, rotation, expected, solution):
    solution.rotate_2(nums, rotation)
    assert nums == expected

@pytest.mark.parametrize(
    "nums, rotation, expected",
    [
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
        ([-1,-100,3,99], 2, [3,99,-1,-100]),
    ]
)
def test_rotate_3(nums, rotation, expected, solution):
    solution.rotate_3(nums, rotation)
    assert nums == expected
