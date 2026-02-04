# 2500. Delete Greatest Value in Each Row
# https://leetcode.com/problems/delete-greatest-value-in-each-row/


def deleteGreatestValue(grid):
    total_sum = 0
    for row in grid:
        row.sort()
    for col in range(len(grid[0])):
        max_in_col = 0
        for row in range(len(grid)):
            max_in_col = max(max_in_col, grid[row][col])
        total_sum += max_in_col
    return total_sum
