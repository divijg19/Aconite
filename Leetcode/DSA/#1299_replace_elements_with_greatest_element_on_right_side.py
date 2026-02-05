# 1299. Replace Elements with Greatest Element on Right Side
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        greatest = -1

        for i in range(n - 1, -1, -1):
            current = arr[i]
            arr[i] = greatest
            if current > greatest:
                greatest = current

        return arr
