from typing import List


class Solution:
    def solution(self, nums: List[int], k: int) -> int:
        score = 0
        max_num = max(nums)
        for i in range(k):
            score += max_num
            max_num += 1
        return score


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 7, 2, 8, 4]
    k = 3

    result = solution.solution(nums, k)
    print("Result：", result)
