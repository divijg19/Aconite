#1. Two Sum
#https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    diff = {}
    for i, num in enumerate(nums):
        if target - num in diff:
            return [diff[target - num], i]
        diff[num] = i
    return []