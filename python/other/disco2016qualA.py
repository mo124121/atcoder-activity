W = int(input())

S = "DiscoPresentsDiscoveryChannelProgrammingContest2016"

N = len(S) // W

for i in range(N):
    print(S[W * i : W * (i + 1)])
if N * W < len(S):
    print(S[N * W :])
