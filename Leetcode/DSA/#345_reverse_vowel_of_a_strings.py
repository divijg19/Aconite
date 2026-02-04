# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/

def reverse_vowels(s):
    vowels = set("aeiouAEIOU")
    s_list = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s_list[left] not in vowels:
            left += 1
        elif s_list[right] not in vowels:
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

    return ''.join(s_list)
