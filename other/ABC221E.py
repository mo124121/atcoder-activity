class FenwickTreeMod:
    def __init__(self, n, mod, init_data=0):
        self.size = n
        self.mod = mod
        self.tree = [0] * (n + 1)
        if init_data != 0:
            for i in range(1, n + 1):
                self.add(i, init_data)

    def sum(self, i):
        ret = 0
        i += 1
        while i > 0:
            ret += self.tree[i]
            ret %= self.mod
            i -= i & -i
        return ret

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            self.tree[i] %= self.mod
            i += i & -i

    def get(self, i):
        return (self.sum(i) - self.sum(i - 1)) % self.mod

    def show(self):
        ret = []
        for i in range(self.size):
            ret.append(self.get(i))
        print(*ret)


def compress(L):
    S = sorted(set(L))  # 配列に含まれるユニークな要素
    d = dict()  # 要素の順位
    i = 0
    for s in S:
        d[s] = i
        i += 1
    ret = []
    for l in L:
        ret.append(d[l] + 1)

    return ret


N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

B = compress(A)
ft = FenwickTreeMod(N + 1, MOD)

ret = 0

inv2 = pow(2, MOD - 2, MOD)

for i, b in enumerate(B):
    ret += ft.sum(b) * pow(2, i, MOD)
    ret %= MOD
    ft.add(b, pow(inv2, i + 1, MOD))

print(ret)

"""
平面走査の基本っぽい
誤読してた

解説AC


"""
