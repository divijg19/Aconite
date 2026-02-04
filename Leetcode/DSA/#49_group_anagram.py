# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            # Sort the string to create a key
            key = "".join(sorted(s))
            anagram_map[key].append(s)

        return list(anagram_map.values())
