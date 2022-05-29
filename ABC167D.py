N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

logK = 61

dp = [[0] * (N + 1) for _ in range(logK + 1)]
dp[0] = A


for k in range(logK):
    for i in range(1, N + 1):
        dp[k + 1][i] = dp[k][dp[k][i]]
ret = 1
for k in range(logK):
    if (K >> k) & 1:
        ret = dp[k][ret]
print(ret)
