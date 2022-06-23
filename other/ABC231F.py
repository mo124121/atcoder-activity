from collections import defaultdict


def compress(L):
    S = sorted(set(L))  # 配列に含まれるユニークな要素
    d = dict()  # 要素の順位
    i = 0
    for s in S:
        d[s] = i
        i += 1
    ret = []
    for l in L:
        ret.append(d[l])

    return ret


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


N = int(input())
A = list(map(int, input().split()))
B = list(map(lambda x: -int(x), input().split()))

Ac = compress(A)
Bc = compress(B)

D = defaultdict(list)
for a, b in zip(Ac, Bc):
    D[a].append(b)

ans = 0
ft = FenwickTree(N)
for a in range(N):
    if len(D[a]) == 0:
        continue
    for b in D[a]:
        ft.add(b, 1)

    for b in D[a]:
        ans += ft.sum(b)
print(ans)


"""
それぞれ相手に対して許容できるプレゼントはbisectでとれる
そのリスト同士の共通部分の個数を算出する
普通にやるとでかすぎる

ギブ
動画解説
片方を負にして反転して、大小関係の添え字を整理する
平面走査


"""
