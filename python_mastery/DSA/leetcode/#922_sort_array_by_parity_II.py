# 922. Sort Array By Parity II
# https://leetcode.com/problems/sort-array-by-parity-ii/

def sort_array_by_parity_ii(nums):
    even_index, odd_index = 0, 1
    n = len(nums)

    while even_index < n and odd_index < n:
        if nums[even_index] % 2 == 0:
            even_index += 2
        elif nums[odd_index] % 2 == 1:
            odd_index += 2
        else:
            nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
            even_index += 2
            odd_index += 2

    return nums

# class Solution:
#     def sortArrayByParityII(self, nums: List[int]) -> List[int]:
#         even=0
#         odd=1
#         while odd<len(nums):
#             if(nums[odd]%2==0):
#                 nums[even],nums[odd]=nums[odd],nums[even]
#                 even+=2
#             else:
#                 odd+=2
#         return nums
