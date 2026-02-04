# Accommodation

# There are B boys and G girls who would like to take accommodation in a hotel.
# The hotel has infinitely many rooms, and each room with a positive number of occupants must satisfy the following conditions:

#     It must contain at least X boys.
#     It must contain at least Y girls.
#     It can contain at most N people in total.

# Determine the minimum number of rooms required to accommodate all B+GB+G people while satisfying these constraints.

# If it is impossible to accommodate everyone while following the constraints, output −1−1.
# Input Format

#     The first line of input will contain a single integer TT, denoting the number of test cases.
#     The first and only line of the each test case contains five space-separated integers B,G,X,Y,NB,G,X,Y,N — the number of boys and girls, the lower bound on boys per room and girls per room, and the maximum number of occupants per room, respectively.

# Output Format

# For each test case, output on a new line the answer: the minimum number of rooms required to accommodate all B+GB+G people while satisfying these constraints, or −1−1 if it's impossible.
# Constraints

#     1≤T≤1051≤T≤105
#     1≤B,G,X,Y,N≤1091≤B,G,X,Y,N≤109

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    B, G, X, Y, N = map(int, input().split())

    if X + Y > N:
        print(-1)
        continue

    Rmin = (B + G + N - 1) // N
    Rmax = min(B // X, G // Y)

    if Rmin > Rmax:
        print(-1)
    else:
        print(Rmin)
