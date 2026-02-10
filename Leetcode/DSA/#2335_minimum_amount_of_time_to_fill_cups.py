# 2335. Minimum Amount of Time to Fill Cups
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/description/

from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        if amount[2] >= amount[0] + amount[1]:
            return amount[2]
        else:
            return (amount[0] + amount[1] + amount[2] + 1) // 2
