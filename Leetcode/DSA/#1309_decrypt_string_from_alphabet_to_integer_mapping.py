# 1309. Decrypt String from Alphabet to Integer Mapping
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

def freqAlphabets(s):
    i = 0
    result = []
    while i < len(s):
        if i + 2 < len(s) and s[i + 2] == '#':
            num = int(s[i:i + 2])
            result.append(chr(num + 96))
            i += 3
        else:
            num = int(s[i])
            result.append(chr(num + 96))
            i += 1
    return ''.join(result)