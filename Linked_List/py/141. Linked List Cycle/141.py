# Problem Description

# 141. Linked List Cycle
# Easy
# Topics
# Companies
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.


# Follow up: Can you solve it using O(1) (i.e. constant) memory?
# 此題可使用快慢指針法來解
#########################################################################################
from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solution1(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        # 設定 fast.next是為了避免快指針出問題
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False


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
