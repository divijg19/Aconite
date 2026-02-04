# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

def sortedSquares(nums):
    result = []
    left, right = 0, len(nums) - 1
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        if left_square > right_square:
            result.append(left_square)
            left += 1
        else:
            result.append(right_square)
            right -= 1
    return result[::-1]