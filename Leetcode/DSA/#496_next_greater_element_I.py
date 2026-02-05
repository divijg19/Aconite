# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        return [next_greater.get(num, -1) for num in nums1]

        # stack = []
        # next_greater = {}

        # for num in reversed(nums2):
        #     while stack and stack[-1] <= num:
        #         stack.pop()
        #     next_greater[num] = -1 if not stack else stack [-1]
        #     stack.append(num)

        # return [next_greater[num] for num in nums1]
