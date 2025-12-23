# 577. Reverse Words in a String III
# link: https://leetcode.com/problems/reverse-words-in-a-string-iii/

# def reverseWords(s):
#     reversed_words = []
#     words = s.split()
#     for word in words:
#         reversed_words.append(word[::-1])
#     return ' '.join(reversed_words)

def reverseWords(s):
    words = s.split(" ")
    reversed_words = []
    for word in words:
        reversed_word = list(word)
        left, right = 0, len(reversed_word) - 1
        while left < right:
            reversed_word[left], reversed_word[right] = reversed_word[right], reversed_word[left]
            left += 1
            right -= 1
        reversed_words.append("".join(reversed_word))
    return ' '.join(reversed_words)