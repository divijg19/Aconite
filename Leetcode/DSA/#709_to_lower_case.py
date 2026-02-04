# 709. To Lower Case
# https://leetcode.com/problems/to-lower-case/


def toLowerCase(s):
    result = ""
    for ch in s:
        if "A" <= ch <= "Z":
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result
