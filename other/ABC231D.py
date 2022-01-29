import sys #追加
sys.setrecursionlimit(500*500) #追加

class UnionFind:
    def __init__(self,N):
        self.parent = [0]*N
        for i in range(N):
            self.parent[i] = i

    def root(self, x):
        if (self.parent[x]==x):
            return x
        else:
            return self.root(self.parent[x])

    def unite(self,x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x==root_y:
            return
        else:
            self.parent[root_x]=root_y

    def same(self,x,y):
        root_x = self.root(x)
        root_y = self.root(y)
        return root_x==root_y


N,M = map(int, input().split())
count={}
uf = UnionFind(N)

ret="Yes"
count = [0]*N
for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1

    for x in (a,b):
        count[x]+=1

    if uf.same(a,b):
        ret = "No"
        break
    uf.unite(a,b)

for i in count:
    if i > 2:
        ret = "No"

print(ret)