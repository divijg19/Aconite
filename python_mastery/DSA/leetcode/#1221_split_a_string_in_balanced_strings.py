# 1221. Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/

def balancedStringSplit(s):
    count = 0
    balance = 0
    for char in s:
        if char == 'L':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            count += 1
    return count