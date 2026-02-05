# 2399. Check Distances Between Same Letters
# https://leetcode.com/problems/check-distances-between-same-letters/


class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        first_occurrence = {}

        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            else:
                expected_distance = distance[ord(char) - ord("a")]
                actual_distance = i - first_occurrence[char] - 1
                if actual_distance != expected_distance:
                    return False

        return True
