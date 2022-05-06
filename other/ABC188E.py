from collections import defaultdict, deque
from heapq import heapify, heappop, heappush


N, M = map(int, input().split())
A = list(map(int, input().split()))

G = defaultdict(list)

for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    G[x].append(y)
INF = 10**11
dp = [INF] * N

for i in range(N):
    for nxt in G[i]:
        dp[nxt] = min(dp[nxt], dp[i], A[i])

ret = -INF
for i in range(1, N):
    ret = max(ret, A[i] - dp[i])
print(ret)

"""
ある町からある町へ移動できるか？

1方向性をどう管理する？
サイクルもあるだろう

順方向から計算した後、逆方向から管理するとか？

解説後
解法1:DAGであることを使う
解法2:最小の街を起点に幅探索　一度見たところは飛ばす

"""
