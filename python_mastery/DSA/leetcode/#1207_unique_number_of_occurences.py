# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/

def uniqueOccurrences(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    occurrences = set()
    for count in freq.values():
        if count in occurrences:
            return False
        occurrences.add(count)
        
    return True