# 2011. Final Value of Variable After Performing Operations
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

def finalValueAfterOperations(operations):
    x = 0
    for op in operations:
        if '+' in op:
            x += 1
        else:
            x -= 1
    return x