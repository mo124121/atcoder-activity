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


N, M = map(int, input().split())
uf = UnionFind(N + 1)
loop = []
for _ in range(M):
    u, v = map(int, input().split())
    if uf.same(u, v):
        loop.append(u)
    else:
        uf.unite(u, v)

compos = set()
for i in range(1, N + 1):
    compos.add(uf.root(i))

for u in loop:
    compos.discard(uf.root(u))

print(len(compos))

"""
ufで閉路になるような連結成分を削りつつ、
そうでない連結成分 = rootの個数をカウントする
AC

ufじゃなくても各点からdfsで到達可能な範囲を一塊にし、
loopが見つかった時点でカウントをやめる、という感じでいい

"""
