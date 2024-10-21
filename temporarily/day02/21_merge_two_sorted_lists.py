"""
You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

(1)--->(2)--->(4)
(1)-->(3)--->(4)
..............
(1)--->(1)--->(2)--->(3)--->(4)--->(4)

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
import pytest
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

def to_linked_list(a_list: List[int]):
    if not a_list:
        return None

    head = ListNode(a_list[0])
    current = head
    for val in a_list[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def to_list(node: Optional[ListNode]):
    result = []
    while node:
        result.append(node.val)
        node = node.next

    return result

@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize(
    'list1, list2, expected',
    [
        ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
        ([], [], []),
        ([], [0], [0]),
    ]
)
def test_merge_two_lists(list1, list2, expected, solution):
    list1 = to_linked_list(list1)
    list2 = to_linked_list(list2)

    merged_list = solution.merge_two_lists(list1, list2)

    result = to_list(merged_list)

    assert result == expected
