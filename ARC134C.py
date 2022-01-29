N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 998244353
rest = sum(A[1:])

if rest + K > A[0]:
    print(0)
    exit()

A[0] -= rest + K

dp = [[0] * (N) for _ in range(K + 1)]

for i in range(N):
    dp[1][i] = 1

for k in range(1, K):
    for i in range(N):
        dp[k + 1][i] = ((dp[k][i] * (A[i] + k))) % MOD

ret = 1
div = 1
for i in range(1, K):
    div *= i
div %= MOD

for i in range(N):
    ret *= dp[K][i] // div
    ret %= MOD

print(ret)
