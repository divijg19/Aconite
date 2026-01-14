# 1588. Sum of all Odd Length Subarrays
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

def sum_odd_length_subarrays(arr):
    n=len(arr)
    sum=0
    for i in range(n):
        sum+=((n-i)*(i+1)+1)//2*arr[i]
    return sum
