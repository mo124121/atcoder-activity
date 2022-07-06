MOD = 10**9 + 7
N, M = map(int, input().split())
A = {}
for i in range(M):
    A[int(input())] = True


dp = [0] * (N + 1)
dp[0] = 1
if 1 not in A:
    dp[1] = 1

for i in range(2, N + 1):
    if i not in A:
        dp[i] = (dp[i - 2] + dp[i - 1]) % MOD

print(dp[N])
