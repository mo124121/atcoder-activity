S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

for i, s in enumerate(S):
    for j, t in enumerate(T):
        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + int(s == t))

ret = []
i = len(S)
j = len(T)
while i and j:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        ret.append(S[i - 1])
        i -= 1
        j -= 1
print(*list(reversed(ret)), sep="")
