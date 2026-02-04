# 20. Valid Parantheses
# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parantheses_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in parantheses_map:
                top_element = stack.pop() if stack else "#"
                if parantheses_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
