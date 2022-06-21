from collections import defaultdict

import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")


class SCC:
    def __init__(self, N, G, Grev) -> None:
        self.order = []
        self.used = [False] * N
        self.group = defaultdict(list)
        self.N = N
        self.G = G
        self.Grev = Grev

    def _dfs(self, s):
        self.used[s] = True
        for t in self.G[s]:
            if not self.used[t]:
                self._dfs(t)
            self.order.append(s)
        
    def _rdfs(self,s,col):
        self.group[col].append(s)
        self.used[s]=True
        for t in self.Grev[s]:
            if not self.used[t]:
                self._rdfs(t,col)

    def run(self):
        for i in range(self.N):
            if not self.used[i]:
                self._dfs(i)
        self.used=[False]*self.N
        count=0
        for s in reversed(self.order):
            if not self.used[s]:
                self._rdfs(s,count)
                count+=1
        return count,self.group


def main():
    N, M = map(int, input().split())

    G = defaultdict(list)
    Grev = defaultdict(list)
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        Grev[b].append(a)

    scc=SCC(N+1,G,Grev)
    count,group=scc.run()
    idx=[0]*(N+1)
    for i in range(count):
        for v in group[i]:
            idx[v]=i

    ans=0
    dp=[0]*(count)
    for i in range(count):
        if len(group[i]==1):
            for v in group[i][0]

    print(ans)


main()
