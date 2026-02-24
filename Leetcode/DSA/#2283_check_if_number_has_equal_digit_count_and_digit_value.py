# 2283. Check if Number Has Equal Digit Count and Digit Value
# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/


class Solution:
    def digitCount(self, num: str) -> bool:
        count = [0] * 10
        for c in num:
            count[int(c)] += 1

        for i, c in enumerate(num):
            if count[i] != int(c):
                return False

        return True
