# 1967. Number of Strings That Appear as Substrings in Word
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/


def numOfStrings(patterns, word):
    count = 0
    for pattern in patterns:
        if pattern in word:
            count += 1
    return count
