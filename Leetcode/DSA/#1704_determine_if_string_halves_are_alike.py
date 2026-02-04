# 1704. Determine if String Halves Are Alike
# https://leetcode.com/problems/determine-if-string-halves-are-alike/


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        mid = len(s) // 2
        first_half = s[:mid]
        second_half = s[mid:]

        count_first = sum(1 for char in first_half if char in vowels)
        count_second = sum(1 for char in second_half if char in vowels)

        return count_first == count_second
