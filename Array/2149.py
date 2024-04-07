# 2149 rearrange-array-elements-by-sign
# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

from typing import List


class Solution:
    def solution1(self, nums: List[int]) -> List[int]:
        # 直接以迴圈歷遍陣列，然後分成正整數和負整數來依序加入

        pos_arr = []
        neg_arr = []

        output_arr = []

        for i in nums:
            if i > 0:
                pos_arr.append(i)
            else:
                neg_arr.append(i)

        for j in range(len(pos_arr)):
            output_arr.append(pos_arr[j])
            output_arr.append(neg_arr[j])

        return output_arr

    def solution2(self, nums: List[int]) -> List[int]:
        # 建立兩個用以指定正整數和負整數位置的pointer，然後便可以把對應的值加入到對應的位置
        # 由於解答是由正整數開始，所以我們給予index 0 ，負整數則是1 這樣我們便可以確保解答陣列會是[p_pos, p_neg, p_pos, p_neg...]
        p_pos = 0
        p_neg = 1

        output_arr = [0] * len(nums)

        for num in nums:
            if num > 0:
                output_arr[p_pos] = num
                p_pos += 2
            else:
                output_arr[p_neg] = num
                p_neg += 2
        return output_arr


if __name__ == "__main__":
    solution = Solution()
    nums = [3, -1, -2, 5, 2, -4]

    result = solution.solution2(nums)
    print("Result：", result)
