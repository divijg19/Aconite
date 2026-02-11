# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(s="", left=0, right=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)

        backtrack()
        return result
