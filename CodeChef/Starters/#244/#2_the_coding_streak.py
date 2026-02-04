# The Coding Streak

# TanMinati loves solving problems.
# You are given an array AA of size NN, where AiAi​ represents the number of problems TanMinati solved on the ii-th day.

# A "streak" is defined as a sequence of consecutive days where TanMinati solves at least 11 problem every day.

# Find the length of the longest streak present among these NN days.
# Input Format

#     The first line of input will contain a single integer TT, denoting the number of test cases.
#     Each test case consists of two lines of input.
#         The first line of each test case contains a single integer NN — the size of the array.
#         The next line contains NN space-separated integers A1,…,ANA1​,…,AN​, where AiAi​ denotes the number of problems solved by TanMinati on ii-th day.

# Output Format

# For each test case, output on a new line the length of the longest streak by TanMinati.
# Constraints

#     1≤T≤1001≤T≤100
#     1≤N≤1001≤N≤100
#     0≤Ai≤1000≤Ai​≤100

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    max_streak = 0
    current_streak = 0

    for problems in A:
        if problems >= 1:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    print(max_streak)
