# Qualified or Not

# TanMinati and Bhavy participated in the first round of a coding competition organized by the Coding Club, IIT Ropar during Advitiya.

# To qualify for the next round, a participant must defeat both TanMinati and Bhavy.

# A participant can defeat another participant by solving at least twice the number of problems as that participant.

# Given that TanMinati solved XX problems and Bhavy solved YY problems, determine whether a participant who solved NN problems can participate in the next round.
# Input Format

#     The first and only line of input will contain three integers NN, XX, and YY, denoting the number of problems solved by the participant, TanMinati, and Bhavy respectively.

# Output Format

# Output YES if the participant qualifies. Otherwise, output NO.

# You may print each character of the string in either uppercase or lowercase (for example, the strings yEs, yes, Yes and YES will all be treated as identical).
# Constraints

#     1≤N,X,Y≤101≤N,X,Y≤10

N, X, Y = map(int, input().split())
if N >= 2 * X and N >= 2 * Y:
    print("YES")
else:
    print("NO")
