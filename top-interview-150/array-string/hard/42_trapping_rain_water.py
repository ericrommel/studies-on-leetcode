"""
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water
it can trap after raining.

Example 1: (See the `rainwatertrap.png` picture attached to this folder)
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""
import pytest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:  # If the height array is empty, no water can be trapped
            return 0

        left, right = 0, len(height) - 1  # Initialize two pointers
        left_max, right_max = height[left], height[right]  # Track max heights on both sides
        water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]  # Update the left maximum
                else:
                    water_trapped += left_max - height[left]  # Add water trapped at current bar
                left += 1  # Move left pointer to the right
            else:
                if height[right] >= right_max:
                    right_max = height[right]  # Update the right maximum
                else:
                    water_trapped += right_max - height[right]  # Add water trapped at current bar
                right -= 1  # Move right pointer to the left

        return water_trapped

@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize(
    "height, expected",
    [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),
    ]
)
def test_trap(height, expected, solution):
    assert solution.trap(height) == expected
