"""
- An advanced way to implement Binary Search.
- Use the element's right neighbor to determine if the condition is met and decide whether to go left or right
- Guarantees Search Space is at least 2 in size at each step
- Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element
  meets the condition.
"""


def binary_search_2(self, nums: list[int], target: int) -> int:
    # Special case
    if len(nums) == 0:
        return -1

    # Init start and end positions
    left, right = 0, len(nums) - 1

    # Search
    while left < right:  # difference 1
        mid = (left + right) // 2  # It can be: left  + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # Searching Right side
        else:
            right = mid  # Searching Left side

    # Post-processing:
    # End Condition: left == right
    if nums[left] == target:
        return left

    return -1
