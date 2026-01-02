# 1. Sum of an array

def sum_array(arr):
    total = 0
    for x in arr:
        total += x
    return total

print("Sum of array [1, 2, 3, 4, 5]:", sum_array([1, 2, 3, 4, 5]))

# 2. Find Maximum Element

def find_max(arr):
    if not arr:
        return None
    max_elem = arr[0]
    for x in arr:
        if x > max_elem:
            max_elem = x
    return max_elem

print("Maximum in array [1, 3, 2, 8, 5]:", find_max([1, 3, 2, 8, 5]))

# 3. Count Occurrences

def count_occ(arr, target):
    count = 0
    for x in arr:
        if x == target:
            count += 1
    return count

print("Occurences of 5 in [4, 5, 6, 5, 7, 7, 8, 2, 3, 6, 5, 5, 0]:", count_occ([4, 5, 6, 5, 7, 7, 8, 2, 3, 6, 5, 5, 0], 5))