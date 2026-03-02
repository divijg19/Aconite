# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index

        return -1
