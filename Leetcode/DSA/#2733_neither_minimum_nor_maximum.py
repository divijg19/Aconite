# 2733. Neither Minimum nor Maximum
# https://leetcode.com/problems/neither-minimum-nor-maximum/description/

from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minnum = min(nums)
        maxnum = max(nums)
        for num in nums:
            if num != minnum and num != maxnum:
                return num
        return -1
