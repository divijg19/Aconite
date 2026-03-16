# 2869. Minimum Operations to Collect Elements
# https://leetcode.com/problems/minimum-operations-to-collect-elements/description/


from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collected = set()
        operations = 0

        # Start from the last element and go backwards
        for i in range(len(nums) - 1, -1, -1):
            operations += 1
            collected.add(nums[i])
            # Stop when all elements from 1 to k are collected
            if all(x in collected for x in range(1, k + 1)):
                return operations

        # If we exit the loop, we didn't find all elements from 1 to k, which should not happen for a valid input
        return operations
