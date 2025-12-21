# 1295. Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

def findNumbers(nums):
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
    return count

print("Count of numbers with even digits in [36, 7990, 6, 2334, 89]:", findNumbers([36, 7990, 6, 2334, 89]))
print("Count of numbers with even digits in [555, 901, 482, 1771]:", findNumbers([555, 901, 482, 1771]))