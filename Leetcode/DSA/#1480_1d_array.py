# 1480. Running Sum of 1D Array
# https://leetcode.com/problems/running-sum-of-1d-array/

def runningSum(nums):
    result= []
    current_sum = 0
    for num in nums:
        current_sum += num
        result.append(current_sum)
    return result

print("Running sum of [1, 3, 5, 7]:", runningSum([1,3,5,7]))
print("Running sum of [2, 4, 6, 8]:", runningSum([2,4,6,8]))