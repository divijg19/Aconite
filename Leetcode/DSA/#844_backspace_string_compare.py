# 844. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/

def backspace_compare(s, t):
    def build_string(string):
        result = []
        for char in string:
            if char == '#':
                if result:
                    result.pop()
            else:
                result.append(char)
        return ''.join(result)

    return build_string(s) == build_string(t)
