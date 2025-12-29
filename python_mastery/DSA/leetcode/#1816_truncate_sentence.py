# 1816. Truncate Sentence
# https://leetcode.com/problems/truncate-sentence/

def truncateSentence(s, k):
    words = s.split()
    return ' '.join(words[:k])