# 283. Move Zeroes
#link: https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums):
    non_zero = 0
    for current in range(len(nums)):
        if nums[current] != 0:
            nums[non_zero], nums[current] = nums[current], nums[non_zero]
            non_zero += 1
    for current in range(non_zero, len(nums)):
        nums[current] = 0