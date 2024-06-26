#Problem Description
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.


#########################################################################################
from typing import List


class Solution:
    def solution1(self, nums: List[int]) -> List[int]:
        # can't use double for loop because O(n)
        # use hash table to check the numbers
        dic = {}

        #O(n)
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        
        #O(n)
        return [i for i in dic.keys() if dic[i] > 1]

if __name__ == "__main__":
    solution = Solution()
    nums = [-5, -1, -1, 2, -2, -5]
    
    result = solution.solution1(nums)
    print("Result：", result)