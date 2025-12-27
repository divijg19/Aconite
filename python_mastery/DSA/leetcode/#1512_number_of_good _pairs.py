# 1512. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/

def numIdenticalPairs(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    good_pairs = 0
    for key in freq:
        count = freq[key]
        good_pairs += (count * (count - 1)) // 2
    return good_pairs