from collections import defaultdict, deque
from heapq import heappush, heappop


class UnionFind:
    def __init__(self, N):

        self.parent = [0] * N
        for i in range(N):
            self.parent[i] = i

    def root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        else:
            self.parent[root_x] = root_y

    def same(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        return root_x == root_y


def No():
    print(-1)
    exit()


N, M = map(int, input().split())
D = list(map(int, input().split()))

# 例外処理系
no_flag = False
if sum(D) != 2 * (N - 1):
    no_flag = True
G = defaultdict(list)
uf = UnionFind(N)

for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)
    D[A] -= 1
    D[B] -= 1
    if uf.same(A, B):
        No()
    uf.unite(A, B)

# 例外処理系
if no_flag:
    No()

ps = [[] for _ in range(N)]
for i in range(N):
    if D[i] < 0:
        No()
    for _ in range(D[i]):
        ps[uf.root(i)].append(i)

hq = []
for i in range(N):
    if len(ps[i]):
        heappush(hq, (-len(ps[i]), i))

ret = []
while len(hq) >= 2:
    si, i = heappop(hq)
    sj, j = heappop(hq)
    ret.append((ps[i].pop() + 1, ps[j].pop() + 1))
    if -si < -sj:
        ps[i], ps[j] = ps[j], ps[i]
    for k in range(len(ps[j])):
        ps[i].append(ps[j][k])

    if -si - sj - 2 > 0:
        heappush(hq, (si + sj + 2, i))


if len(ret) != N - M - 1:
    No()

for r in ret:
    print(*r)
