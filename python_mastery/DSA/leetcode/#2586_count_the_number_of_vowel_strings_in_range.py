# 2586. Count the Number of Vowel Strings in Range
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/


class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels = set("aeiou")
        count = 0

        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1

        return count
