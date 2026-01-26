# 2315. Counting Asterisks
# https://leetcode.com/problems/counting-asterisks/


class Solution:
    def countAsterisks(self, s: str) -> int:
        in_pair = False
        asterisk_count = 0

        for char in s:
            if char == "|":
                in_pair = not in_pair
            elif char == "*" and not in_pair:
                asterisk_count += 1

        return asterisk_count
