# 2729. Check if the Number is Fascinating
# https://leetcode.com/problems/check-if-the-number-is-fascinating/


class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(2 * n) + str(3 * n)
        return set(s) == {"1", "2", "3", "4", "5", "6", "7", "8", "9"} and len(s) == 9
