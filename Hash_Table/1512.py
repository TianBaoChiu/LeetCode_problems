#Problem Description
# 1512. Number of Good Pairs

# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0


# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


#########################################################################################
from typing import List


class Solution:
    def solution1(self, nums: List[int]) -> int:
        dic = {}
        count = 0

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else :
                count = count + dic[num]
                dic[num] += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,1]
    
    result = solution.solution1(nums)
    print("Result：", result)