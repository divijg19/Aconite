# 2418. Sort the People
# https://leetcode.com/problems/sort-the-people/


def sortPeople(names, heights):
    paired = list(zip(heights, names))
    paired.sort(reverse=True)
    sorted_names = [name for height, name in paired]
    return sorted_names
