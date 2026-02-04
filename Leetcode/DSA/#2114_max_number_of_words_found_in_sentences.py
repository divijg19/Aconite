# 2114. Max Number of Words Found in Sentences
# https://leetcode.com/problems/max-number-of-words-found-in-sentences/


def mostWordsFound(sentences):
    max_words = 0
    for sentence in sentences:
        word_count = len(sentence.split())
        if word_count > max_words:
            max_words = word_count
    return max_words
