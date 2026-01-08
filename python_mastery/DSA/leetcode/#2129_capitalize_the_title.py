# 2129. Capitalize the Title
# https://leetcode.com/problems/capitalize-the-title/

def capitalize_title(title):
    words = title.split()
    capitalized_words = []

    for word in words:
        if len(word) <= 2:
            capitalized_words.append(word.lower())
        else:
            capitalized_words.append(word.capitalize())

    return ' '.join(capitalized_words)
