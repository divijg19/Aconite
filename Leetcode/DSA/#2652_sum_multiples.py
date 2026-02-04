# 2652. Sum Multiples
# https://leetcode.com/problems/sum-multiples/

def sum_multiples(n):
    f = lambda k: k * (n // k) * (n // k + 1) // 2
    return f(3) + f(5) + f(7) - f(15) - f(21) - f(35) + f(105)
