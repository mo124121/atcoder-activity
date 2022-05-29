from collections import defaultdict


class FenwickTree:
    def __init__(self, n, init_data=0):
        self.size = n
        self.tree = [0] * (n + 1)
        if init_data != 0:
            for i in range(1, n + 1):
                self.add(i, init_data)

    def sum(self, i):
        ret = 0
        i += 1
        while i > 0:
            ret += self.tree[i]
            i -= i & -i
        return ret

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def get(self, i):
        return self.sum(i) - self.sum(i - 1)

    def lower_bound(self, w):
        if w <= 0:
            return 0
        x = 0
        r = 1
        while r < self.size:
            r = r << 1
        length = r
        S = 0
        while length > 0:
            if length + x < self.size and self.tree[x + length] < w:
                w -= self.tree[x + length]
                x += length
            length = length >> 1
        return x

    def show(self):
        ret = []
        for i in range(self.size):
            ret.append(self.get(i))
        print(*ret)


class RangedFenwick:
    def __init__(self, n, init_data=0) -> None:
        self.ft0 = FenwickTree(n + 1, init_data=init_data)
        self.ft1 = FenwickTree(n + 1)
        self.size = n

    def add_range(self, l, r, x):
        l += 1
        r += 1
        self.ft0.add(l, -x * (l - 1))
        self.ft0.add(r + 1, x * r)
        self.ft1.add(l, x)
        self.ft1.add(r + 1, -x)

    def add(self, i, x):
        self.ft0.add(i, x)

    def sum(self, i):
        return self.ft0.sum(i) + self.ft1.sum(i) * i

    def get(self, i):
        return self.sum(i + 1) - self.sum(i)

    def show(self):
        ret = []
        for i in range(self.size):
            ret.append(self.get(i))
        print(*ret)


N, M, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]

rft = RangedFenwick(N + 1)
# 先読みしてリセットする対応を探す
seen = defaultdict(list)
target = [set() for _ in range(Q)]
for i in range(Q - 1, -1, -1):
    q = queries[i]
    if q[0] == 3:
        seen[q[1]].append(i)
    elif q[0] == 2:
        if q[1] in seen:
            target[i].update(seen[q[1]])
            seen[q[1]] = []

ret = []
ret_tmp = [0] * Q
for i in range(Q):
    q = queries[i]
    if q[0] == 1:
        rft.add_range(q[1] - 1, q[2], q[3])
    elif q[0] == 2:
        for t in target[i]:
            j = queries[t][2]
            ret_tmp[t] -= rft.get(j) + q[2]
    else:
        j = queries[i][2]
        ret.append(rft.get(j) - ret_tmp[i])
print(*ret, sep="\n")


"""
ベースはfenwickで管理

クエリ先読みして、全体置き換え時に最終的に反映される要素のmapを持っておく
出力の段階が来たら合計の辻褄合わせをする

あわんわ


"""
