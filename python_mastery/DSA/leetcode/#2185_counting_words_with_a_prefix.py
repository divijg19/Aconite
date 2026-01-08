# 2185. Counting Words With a Given Prefix
# https://leetcode.com/problems/counting-words-with-a-given-prefix/

def prefix_count(words, pref):
    count = 0
    pref_length = len(pref)

    for word in words:
        if word[:pref_length] == pref:
            count += 1

    return count

#   for word in words:
#         if word.startswith(pref):
#             count += 1
#   return count
