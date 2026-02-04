# 2176. Count Equal and Divisible Pairs in an Array
# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/


def countPairs(nums, k) -> int:
    res = 0
    data = {}

    for j in range(len(nums)):
        req = data.get(nums[j], [])
        for i in req:
            if (i * j) % k == 0:
                res += 1
        req.append(j)
        data[nums[j]] = req

    return res


# class Solution:
#     def countPairs(nums, k) -> int
#         res = 0
#         data = defaultdict(list)

#         for j in range(len(nums)):
#             req = data[nums[j]]
#             for i in req:
#                 if (i * j) % k == 0:
#                     res += 1
#             data[nums[j]].append(j)

#         return res
