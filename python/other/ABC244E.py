N, M, K, S, T, X = map(int, input().split())
MOD = 998244353

from collections import defaultdict

G = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dp = [[[0] * (N + 1) for _ in range(K + 1)] for _ in range(2)]
dp[0][0][S] = 1

for k in range(K):
    for i in range(1, N + 1):
        for nxt in G[i]:
            dp[int(nxt == X)][k + 1][nxt] += dp[0][k][i]
            dp[int(nxt == X)][k + 1][nxt] %= MOD
            dp[1 - int(nxt == X)][k + 1][nxt] += dp[1][k][i]
            dp[1 - int(nxt == X)][k + 1][nxt] %= MOD

print(dp[0][K][T])
