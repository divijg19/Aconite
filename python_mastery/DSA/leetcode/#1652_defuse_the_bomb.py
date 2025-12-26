# 1652. Defuse the Bomb
# https://leetcode.com/problems/defuse-the-bomb/

def decrypt(code, k):
    n = len(code)
    if k == 0:
        return [0] * n
    result = []
    for i in range(n):
        total = 0
        if k > 0:
            for j in range(1, k + 1):
                total += code[(i + j) % n]
        else:
            for j in range(1, abs(k) + 1):
                total += code[(i - j + n) % n]
        result.append(total)
    return result