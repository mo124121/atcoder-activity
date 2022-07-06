#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


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


class Solver:
    def __init__(self, H, W) -> None:
        self.stat = [[False] * (2 + W) for _ in range(H + 2)]
        self.W = W + 2
        self.H = H + 2
        self.uf = UnionFind((H + 2) * (W + 2))

    def fill_red(self, r, c):
        self.stat[r][c] = True
        self.connect(r, c, r + 1, c)
        self.connect(r, c, r - 1, c)
        self.connect(r, c, r, c + 1)
        self.connect(r, c, r, c - 1)

    def connect(self, ra, ca, rb, cb):
        if self.stat[rb][cb] == True:
            self.uf.unite(self.W * ra + ca, self.W * rb + cb)

    def check(self, ra, ca, rb, cb):
        if (
            self.uf.same(self.W * ra + ca, self.W * rb + cb)
            and self.stat[rb][cb]
            and self.stat[ra][ca]
        ):
            return YES
        else:
            return NO


def main():
    H, W = map(int, input().split())
    Q = int(input())
    solver = Solver(H, W)
    ret = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            solver.fill_red(query[1], query[2])
        else:
            ret.append(solver.check(query[1], query[2], query[3], query[4]))

    print(*ret, sep="\n")


if __name__ == "__main__":
    main()
