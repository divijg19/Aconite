# 1694. Reformat Phone Number
# https://leetcode.com/problems/reformat-phone-number/


class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = [char for char in number if char.isdigit()]
        reformatted = []
        i = 0

        while i < len(digits):
            if len(digits) - i > 4:
                reformatted.append("".join(digits[i : i + 3]))
                i += 3
            elif len(digits) - i == 4:
                reformatted.append("".join(digits[i : i + 2]))
                reformatted.append("".join(digits[i + 2 : i + 4]))
                break
            else:
                reformatted.append("".join(digits[i:]))
                break

        return "-".join(reformatted)
