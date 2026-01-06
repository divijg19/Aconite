# 1913. Max Product Difference Between Two Pairs
# https://leetcode.com/problems/max-product-difference-between-two-pairs/


def max_product_difference(nums):
    nums.sort()

    return nums[-1] * nums[-2] - nums[0] * nums[1]
