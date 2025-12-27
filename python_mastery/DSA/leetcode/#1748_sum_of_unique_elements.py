# 1748. Sum of Unique Elements
# https://leetcode.com/problems/sum-of-unique-elements/

def sumOfUnique(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
        
    total = 0
    for key in freq:
        if freq[key] == 1:
            total += key
    return total