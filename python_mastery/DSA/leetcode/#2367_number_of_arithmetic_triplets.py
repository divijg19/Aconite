# 2367. Number of Arithmetic Triplets
# https://leetcode.com/problems/number-of-arithmetic-triplets/

def arithmeticTriplets(nums, diff):
    num = set(nums)
    count = 0
    for n in nums:
        if n + diff in num and n + 2 * diff in num:
            count += 1
    return count