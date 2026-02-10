# 1636. Sort Array by Increasing Frequency
# https://leetcode.com/problems/sort-array-by-increasing-frequency/

from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))
