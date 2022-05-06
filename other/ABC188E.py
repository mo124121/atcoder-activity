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

seen = set()
h = [(A[i], i) for i in range(N)]
heapify(h)
ret = -(10**11)
while len(h):
    a, i = heappop(h)
    if i in seen:
        continue
    q = deque()
    q.append(i)
    while len(q):
        j = q.popleft()

        for nxt in G[j]:
            if nxt not in seen:
                q.append(nxt)
                ret = max(ret, A[nxt] - a)
                seen.add(nxt)

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
