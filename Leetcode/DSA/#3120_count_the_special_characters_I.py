# 3120. Count the special characters I
# https://leetcode.com/problems/count-the-special-characters-i/

# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
# Return the number of special letters in word.


class Solution:
    def countSpecialCharacters(self, word: str) -> int:
        lower_seen = set()
        upper_seen = set()

        for char in word:
            if char.islower():
                lower_seen.add(char)
            elif char.isupper():
                upper_seen.add(char.lower())

        # Special characters are those that appear in both lowercase and uppercase
        special_count = len(lower_seen & upper_seen)  # Set intersection
        return special_count
