# 1431. Kids with the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    greatest = []
    for candy in candies:
        if candy + extraCandies >= max_candies:
            greatest.append(True)
        else:
            greatest.append(False)
    return greatest

print("Kids with greatest candies in [2,3,5,1,3] with 3 extra candies:", kidsWithCandies([2,3,5,1,3], 3))
print("Kids with greatest candies in [4,2,1,1,2] with 1 extra candy:", kidsWithCandies([4,2,1,1,2], 1))