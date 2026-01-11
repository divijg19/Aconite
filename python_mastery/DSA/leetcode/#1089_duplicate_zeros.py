# 1089. Duplicate Zeros

from typing import List
def duplicate_zeros(arr: List[int]) -> None:
    n = len(arr)
    i = 0

    while i < n:
        if arr[i] == 0:
            arr.insert(i + 1, 0)
            arr.pop()  # Remove the last element to maintain the size
            i += 2  # Skip the next zero we just added
        else:
            i += 1
