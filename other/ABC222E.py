N, M, K = map(int, input().split())
A = list(map(int, input().split()))
from collections import Counter, defaultdict, deque

G = defaultdict(list)
for i in range(N - 1):
    u, v = map(int, input().split())
    G[u].append((v, i))
    G[v].append((u, i))

count = Counter()


def dfs(node, goal, par=-1):
    if node == goal:
        return True

    for nxt, edge in G[node]:
        if nxt != par:
            ret = dfs(nxt, goal, node)
            if ret:
                count[edge] += 1
                return True

    return False


for i in range(M - 1):
    s = A[i]
    t = A[i + 1]
    dfs(s, t)


# dpでの数え上げ
dp = Counter()
dp[0] = 1
MOD = 998244353
for i in range(N - 1):
    if count[i] == 0:
        for k in dp.keys():
            dp[k] *= 2
            dp[k] %= MOD
    else:
        r = count[i]
        nxt = Counter()
        for k, c in dp.items():
            nxt[k + r] += c
            nxt[k + r] %= MOD
            nxt[k - r] += c
            nxt[k - r] %= MOD
        dp = nxt

print(dp[K] % MOD)
