S = input()
N = len(S)
logK = 20

dp = [[0] * N for _ in range(logK + 1)]

for i in range(N):
    if S[i] == "R":
        dp[0][i] = i + 1
    else:
        dp[0][i] = i - 1

for k in range(logK):
    for i in range(N):
        dp[k + 1][i] = dp[k][dp[k][i]]

pos = [i for i in range(N)]

for i in range(N):
    for k in range(logK):
        if (10**6 >> k) & 1:
            pos[i] = dp[k][pos[i]]

ret = [0] * N
for p in pos:
    ret[p] += 1

print(*ret)
