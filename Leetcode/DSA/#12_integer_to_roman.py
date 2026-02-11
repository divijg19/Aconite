# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ""
        for i in range(len(val)):
            count = num // val[i]
            roman_num += syms[i] * count
            num -= val[i] * count
        return roman_num
