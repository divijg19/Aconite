# 2558. Take Gifts From the Richest Pile
# https://leetcode.com/problems/take-gifts-from-the-richest-pile/

from typing import List
import heapq
from math import floor, sqrt


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            n = -heapq.heappop(gifts)

            heapq.heappush(gifts, -floor(sqrt(n)))

        return -sum(gifts)
