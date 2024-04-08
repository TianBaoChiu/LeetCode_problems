#Problem Description
# 242. Valid Anagram
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letter


#########################################################################################
from typing import List


class Solution:
    def solution1(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_dic = {}
        t_dic = {}

        for s_letter in s:
            if s_letter not in s_dic:
                s_dic[s_letter] = 1
            else:
                s_dic[s_letter] +=1
        
        for t_letter in t:
            if t_letter not in t_dic:
                t_dic[t_letter] = 1
            else:
                t_dic[t_letter] +=1

        for s_letter in s:
            if (s_letter not in t_dic) or (s_dic[s_letter] != t_dic[s_letter]):
                return False
            
        return True


if __name__ == "__main__":
    solution = Solution()
    s = "rat"
    t = "car"
    
    result = solution.solution1(s, t)
    print("Result：", result)