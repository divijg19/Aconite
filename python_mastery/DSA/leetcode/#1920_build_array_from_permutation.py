# 1920. Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/

def buildArray(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans