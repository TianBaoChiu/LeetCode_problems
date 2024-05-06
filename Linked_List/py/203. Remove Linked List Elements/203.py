# Problem Description
# 203. Remove Linked List Elements
# Easy
# Topics
# Companies
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []


# Constraints:

# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

#########################################################################################
from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solution1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Your solution goes here
        pre_node = None
        current_node = head
        # 遍歷整個鏈結串列
        while current_node:
            # 找到目標節點
            if current_node.val == val:
                # 檢查是否為頭節點，如果不是就把前一個節點的next改為下一個節點，跳過當前節點
                if pre_node:
                    pre_node.next = current_node.next
                else:
                    # 頭節點的話則可以直接變更頭節點的位置
                    head = current_node.next
                current_node = current_node.next
            else:
                # 沒找到目標節點就繼續前進 1. pre_node需要跟上current_node 2.current_node需要往前一個節點
                pre_node = current_node
                current_node = current_node.next

        return head


if __name__ == "__main__":
    solution = Solution()
    inputs = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    expected_output = [1, 2, 3, 4, 5]

    solution_func = "solution1"

    output = getattr(solution, solution_func)(inputs, val)

    if output == expected_output:
        print(
            f"Input: {solution_func}({', '.join(map(str, inputs))}), Output: {output}"
        )
    else:
        print(
            f"Input: {solution_func}({', '.join(map(str, inputs))}), Expected: {expected_output}, Got: {output}"
        )
