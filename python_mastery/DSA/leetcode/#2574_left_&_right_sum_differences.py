# 2574. Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/


def left_right_difference(nums):
    n = len(nums)
    left_sum = [0] * n
    right_sum = [0] * n
    result = [0] * n

    # Calculate left sums
    for i in range(1, n):
        left_sum[i] = left_sum[i - 1] + nums[i - 1]

    # Calculate right sums
    for i in range(n - 2, -1, -1):
        right_sum[i] = right_sum[i + 1] + nums[i + 1]

    # Calculate the absolute differences
    for i in range(n):
        result[i] = abs(left_sum[i] - right_sum[i])

    return result
