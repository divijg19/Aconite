# 2859. Sum of Values of Indices With K Set Bits
# https://leetcode.com/problems/sum-of-values-of-indices-with-k-set-bits/

def sum_indices_with_k_set_bits(nums, k):
    total_sum = 0

    for i in range(len(nums)):
        if bin(i).count('1') == k:
            total_sum += nums[i]

    return total_sum
