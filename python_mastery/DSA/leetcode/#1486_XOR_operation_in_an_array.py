# 1486. XOR Operation in an Array
# https://leetcode.com/problems/xor-operation-in-an-array/

def xorOperation(n, start):
    result = 0
    for i in range(n):
        result ^= start + 2 * i
    return result