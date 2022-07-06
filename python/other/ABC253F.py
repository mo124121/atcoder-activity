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

last_update = {}
score_event = defaultdict(list)
for t, query in enumerate(queries):
    if query[0] == 2:
        _, i, x = query
        last_update[i] = t
    if query[0] == 3:
        _, i, j = query
        if i in last_update:
            score_event[last_update[i]].append((t, j))


rft = RangedFenwick(M + 1)

ret = []
offset = {}
for t, query in enumerate(queries):
    query = queries[t]
    if query[0] == 1:
        _, l, r, x = query
        rft.add_range(l, r, x)
    elif query[0] == 2:
        _, i, x = query
        if t in score_event:
            for q2, j in score_event[t]:
                offset[q2] = x - rft.get(j)
    else:
        _, i, j = query
        tmp = rft.get(j)
        if t in offset:
            tmp += offset[t]
        ret.append(tmp)

print(*ret, sep="\n")


"""
ベースはfenwickで管理

クエリ先読みして、全体置き換え時に最終的に反映される要素のmapを持っておく
出力の段階が来たら合計の辻褄合わせをする

あわんわ


"""
