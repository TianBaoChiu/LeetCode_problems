# Problem Description
# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


#########################################################################################
from typing import List


class Solution:
    def solution1(self, s: str) -> bool:

        char_stack = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                char_stack.append(char)
            else:
                print(char_stack)
                print(char)
                if char_stack[-1] == "(" and char == ")":
                    char_stack.pop()
                elif char_stack[-1] == "[" and char == "]":
                    char_stack.pop()
                elif char_stack[-1] == "{" and char == "}":
                    char_stack.pop()
                else:
                    return False

        return not char_stack

    def solution2(self, s: str) -> bool:
        # use stack structure too, but try to run faster in python 3

        char_stack = []

        for char in s:
            if char in "([{":
                char_stack.append(char)
            else:
                if (
                    not char_stack
                    or (char == ")" and char_stack[-1] != "(")
                    or (char == "]" and char_stack[-1] != "[")
                    or (char == "}" and char_stack[-1] != "{")
                ):
                    return False
                char_stack.pop()

        return not char_stack


if __name__ == "__main__":
    solution = Solution()
    s = "()"

    result = solution.solution2(s)
    print("Result：", result)
