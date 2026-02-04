# 1470. Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/

def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result

print("Shuffled array of [2,5,1,3,4,7] with n=3:", shuffle([2,5,1,3,4,7], 3))
print("Shuffled array of [1,2,3,4,4,3,2,1] with n=4:", shuffle([1,2,3,4,4,3,2,1], 4))