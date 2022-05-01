from collections import Counter
from heapq import heappop, heappush


H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = []
for h in range(H):
    A += list(map(int, input().split()))
count = Counter(A)
INF = 10**10
cost = [INF] * 10
cost[1] = 0
h = []
heappush(h, (0, 1))
finalized = set()
while len(h):
    c, node = heappop(h)
    if node in finalized:
        continue
    finalized.add(node)
    cost[node] = c
    for neibor in range(10):
        if neibor not in finalized:
            heappush(h, (c + C[neibor][node], neibor))

ret = 0
for k, v in count.items():
    if k == -1:
        continue
    ret += v * cost[k]
print(ret)

"""
とりあえず各数の出現数をカウント

ある数字を1に変える最小コストを算出
どうだす？グラフの問題くさい
1からほかの数字への最小コストを計算でもいい、ダイクストラ的な？


"""
