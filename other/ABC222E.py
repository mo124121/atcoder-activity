N, M, K = map(int, input().split())
A = list(map(int, input().split()))
from collections import Counter, defaultdict, deque

G = defaultdict(list)
for i in range(N - 1):
    u, v = map(int, input().split())
    G[u].append((v, i))
    G[v].append((u, i))

count = Counter()

for i in range(M - 1):
    s = A[i]
    t = A[i + 1]
    q = deque()
    q.append((s, 0))
    seen = {}
    seen[s] = 0
    # 最短経路の把握
    while q:
        node, d = q.popleft()
        if node == t:
            break
        for nxt, _ in G[node]:
            if nxt not in seen:
                q.append((nxt, d + 1))
                seen[nxt] = d + 1

    # 経路復元　各辺の通過回数のカウント
    q.clear()
    q.append((t, d))
    while q:
        node, d = q.popleft()
        if node == s:
            break
        for nxt, edge in G[node]:
            if nxt in seen and seen[nxt] == d - 1:
                q.append((nxt, d - 1))
                count[edge] += 1

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
