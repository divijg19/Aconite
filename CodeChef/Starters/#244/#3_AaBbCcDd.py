# AabBcCDd

# During Advitiya, the Coding Club is designing a digital banner made up of English letters.
# Each letter can appear in either uppercase or lowercase.

# You are given a string SS of length NN, denoting the current state of the banner.

# To maintain visual uniformity, the design team allows the following two types of transformations:

#     Operation 11: You may convert any uppercase letter to its corresponding lowercase letter.
#     Formally, choose an index ii (1≤i≤N1≤i≤N) such that SiSi​ is an uppercase letter, and convert it to the corresponding lowercase letter (so A→a,B→bA→a,B→b, and so on.)
#         This operation can be performed any number of times.
#     Operation 22: You may choose exactly one lowercase letter and convert all of its occurrences into another lowercase letter.
#     For example, if S="aAbaCad"S="aAbaCad", converting all the occurrences of ’a’’a’ into ’e’’e’ will result in the string "eAbeCed""eAbeCed".
#         This operation can be performed only once.

# The score of the banner is defined to be the maximum number of occurrences of any single lowercase letter present in it.
# For example, the score of "aAbaCad""aAbaCad" is 33, because the character ’a’’a’ appears three times.

# Find the maximum possible score the banner can attain by performing the above operations.
# Note that the second type of operation can only be performed once, while the first type can be performed any number of times.
# Input Format

#     The first line of input will contain a single integer TT, denoting the number of test cases.
#     Each test case consists of two lines of input.
#         The first line of each test case contains a single integer NN, representing the length of the banner string.
#         The second line contains a string SS of length NN, denoting the initial banner string.

# Output Format

# For each test case, output a single integer denoting the maximum possible occurrences of any one lowercase letter after applying the operations.
# Constraints

#     1≤T≤10001≤T≤1000
#     1≤N≤1001≤N≤100
#     SS consists only of uppercase and lowercase English letters.

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()

    # Count lowercase frequencies after converting everything to lowercase
    freq = [0] * 26
    for ch in S:
        freq[ord(ch.lower()) - ord("a")] += 1

    # Sort frequencies descending
    freq.sort(reverse=True)

    # Best possible score
    if freq[1] > 0:
        print(freq[0] + freq[1])
    else:
        print(freq[0])
