# 1897. Redistribute Characters to Make All Strings Equal
# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)

        combined = "".join(words)
        for c in set(combined):
            if combined.count(c) % n != 0:
                return False
        return True
