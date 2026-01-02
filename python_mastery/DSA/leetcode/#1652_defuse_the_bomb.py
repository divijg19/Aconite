# 1652. Defuse the Bomb
# https://leetcode.com/problems/defuse-the-bomb/

def decrypt(code, k):
        n = len(code)
        if k == 0:
            return [0] * n
        res = []
        decrypt = 0
        if k > 0:
            for i in range(k):
                if (i + 1) > k:
                    decrypt += code[(i + 1) % n]
                else:
                    decrypt += code[i + 1]
            res.append(decrypt)

            for i in range(1, n):
                decrypt -= code[i]
                decrypt += code[(i + k) % n]
                res.append(decrypt)
            return res

        if k < 0:
            for i in range(0, abs(k)):
                decrypt += code[n - i - 1]
            res.append(decrypt)

            for i in range(1, n):
                decrypt -= code[(i - 1 + k)]
                decrypt += code[i - 1]
                res.append(decrypt)
            return res