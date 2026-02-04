# 2778. Sum of Squares of Special Elements
# https://leetcode.com/problems/sum-of-squares-of-special-elements/

from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            if len(nums) % (i + 1) == 0:
                total += nums[i] ** 2
        return total
