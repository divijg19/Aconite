# 3745. Maximize Expression of Three Elements
# https://leetcode.com/problems/maximize-expression-of-three-elements/description/

from typing import List
from heapq import nlargest


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        return sum(nlargest(2, nums)) - min(nums)
