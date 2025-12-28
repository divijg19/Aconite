# 1464. Maximum Product of Two Elements in an Array
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

def maxProduct(nums):
    nums.sort()
    return (nums[-1] - 1) * (nums[-2] - 1)