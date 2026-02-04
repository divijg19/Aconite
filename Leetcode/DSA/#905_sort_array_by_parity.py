# 905. Sort Array By Parity
# https://leetcode.com/problems/sort-array-by-parity/

def sort_array_by_parity(nums):
    return [num for num in nums if num % 2 == 0] + [num for num in nums if num % 2 != 0]
