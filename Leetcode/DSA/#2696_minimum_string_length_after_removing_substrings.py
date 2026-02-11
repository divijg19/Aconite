# 2696. Minimum String Length After Removing Substrings
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/


class Solution:
    def minLength(self, s: str) -> int:
        stack = [s[0]]
        for ch in s[1:]:
            prev = stack[-1] if stack else None
            curr = ch
            if (prev == "A" and curr == "B") or (prev == "C" and curr == "D"):
                stack.pop()
            else:
                stack.append(curr)
        return len(stack)
