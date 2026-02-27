# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_consecutive = 0
        current_consecutive = 0

        for num in nums:
            if num == 1:
                current_consecutive += 1
            else:
                max_consecutive = max(max_consecutive, current_consecutive)
                current_consecutive = 0

        return max(max_consecutive, current_consecutive)
