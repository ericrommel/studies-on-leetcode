"""
Given a string `s`, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
import pytest


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize(
    's, expected',
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ]
)
def test_length_of_longest_substring(s, expected, solution):
    assert solution.length_of_longest_substring(s) == expected
