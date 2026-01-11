# 917. Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/

def reverse_only_letters(s):
    letters = [c for c in s if c.isalpha()]
    result = []

    for c in s:
        if c.isalpha():
            result.append(letters.pop())
        else:
            result.append(c)

    return ''.join(result)
