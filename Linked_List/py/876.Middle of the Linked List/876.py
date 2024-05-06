# Problem Description
# 876. Middle of the Linked List
# Easy
# Topics
# Companies
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# 該題會使用到快慢指針法解題
#########################################################################################
from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solution1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        # 當快指針的值為空或是下一個值為空，代表鏈結串列到底了
        while curr and curr.next:
            # 慢指針
            head = head.next
            # 快指針
            curr = curr.next.next

        return head


if __name__ == "__main__":
    solution = Solution()
    inputs = []
    expected_output = []

    solution_func = "solution1"

    output = getattr(solution, solution_func)(inputs)

    if output == expected_output:
        print(
            f"Input: {solution_func}({', '.join(map(str, inputs))}), Output: {output}"
        )
    else:
        print(
            f"Input: {solution_func}({', '.join(map(str, inputs))}), Expected: {expected_output}, Got: {output}"
        )
