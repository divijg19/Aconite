# 2068. Check Whether Two Strings Are Almost Equivalent
# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        char_count = {}

        for char in word1:
            char_count[char] = char_count.get(char, 0) + 1

        for char in word2:
            char_count[char] = char_count.get(char, 0) - 1

        return all(-3 <= count <= 3 for count in char_count.values())
