# 1844. Replace All Digits with Characters
# https://leetcode.com/problems/replace-all-digits-with-characters/

def replaceDigits(s):
    result = ""
    last_char = 0
    for ch in s:
        if ch.isalpha():
            result += ch
            last_char = ord(ch)
        else:
            result += chr(last_char + int(ch))
    return result