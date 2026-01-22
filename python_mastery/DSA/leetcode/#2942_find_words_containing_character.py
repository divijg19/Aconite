# 2942. Find Words Containing Character
# https://leetcode.com/problems/find-words-containing-a-character/

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], ch: str) -> List[str]:
        result = []
        for word in range(len(words)):
            if ch in words[word]:
                result.append(word)
        return result
