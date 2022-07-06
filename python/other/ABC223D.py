from heapq import heappop, heappush


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
d = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    d[b] += 1

h = []
for i in range(1, N + 1):
    if d[i] == 0:
        heappush(h, i)

ret = []
while len(h):
    v = heappop(h)
    ret.append(v)
    for n in G[v]:
        d[n] -= 1
        if d[n] == 0:
            heappush(h, n)

if len(ret) == N:
    print(*ret)
else:
    print(-1)
"""
考察

N,M<10**5
O(NlogN)あたり

1条件を満たしつつ最小なのは何か？
1 2 3 4
制約2 1
2 1 3 4
制約3 4
2 1 3 4
制約 2 4

たぶんBの直後にずらすのがいい

どういう時が満たせないか？
2 1
1 2
矛盾する時、ただ必ずしも同時にはでてこない
1 2
2 3
3 4
4 1

条件でソートしたらどうなる？

in1
4 3
2 1
3 4
2 4

グラフ？
グラフとしてとらえるとどうなる？
条件は進む方向を規定している
なんかトポロジカルソートっぽくね？

4 3
3 2 
2 1


解説後
これ初見じゃないわ

"""
