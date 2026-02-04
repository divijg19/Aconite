# 2108. Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

def first_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""
