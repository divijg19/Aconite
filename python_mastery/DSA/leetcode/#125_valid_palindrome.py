# 125. Valid Palindrome
#link: https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    return True
