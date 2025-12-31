# 1859. Sorting the Sentence
# https://leetcode.com/problems/sorting-the-sentence/

def sortSentence(s):
    words = s.split()
    sorted = [''] * len(words)
    
    for word in words:
        index = int(word[-1])
        sorted[index-1] = word[:-1]
        
    return ' '.join(sorted)