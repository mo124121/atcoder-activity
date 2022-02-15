import sys  # 追加

sys.setrecursionlimit(500 * 500)  # 追加


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


class SegmentTree:
    def __init__(self, N, INF=-1) -> None:
        n = 1
        while n < N:
            n <<= 1

        self.n = n
        self.INF = INF
        self.elements = [INF] * (2 * n - 1)

    def update(self, i, x):
        i += self.n - 1
        self.elements[i] = x
        while i > 0:
            i = (i - 1) // 2
            self.elements[i] = max(self.elements[i * 2 + 1], self.elements[i * 2 + 2])

    def query(self, a, b):
        return self._query_rec(a, b, 0, 0, self.n)

    def _query_rec(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.INF
        elif a <= l and r <= b:
            return self.elements[k]
        else:
            vl = self._query_rec(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self._query_rec(a, b, k * 2 + 2, (l + r) // 2, r)
            return max(vl, vr)


class LazySegmentTree:
    def __init__(self, N, INF=0) -> None:
        n = 1
        while n < N:
            n *= 2

        self.n = n
        self.INF = INF
        self.elements = [INF] * (2 * n - 1)
        self.lazy = [INF] * (2 * n - 1)

    def eval(self, k):
        if self.lazy[k] == self.INF:
            return
        if k < self.n - 1:
            self.lazy[k * 2 + 1] = self.lazy[k]
            self.lazy[k * 2 + 2] = self.lazy[k]

        self.elements[k] = self.lazy[k]
        self.lazy[k] = self.INF

    def query(self, a, b):
        return self._query_rec(a, b, 0, 0, self.n)

    def _query_rec(self, a, b, k, l, r):
        self.eval(k)
        if r <= a or b <= l:
            return self.INF
        elif a <= l and r <= b:
            return self.elements[k]
        else:
            vl = self._query_rec(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self._query_rec(a, b, k * 2 + 2, (l + r) // 2, r)
            return max(vl, vr)

    def update(self, a, b, x):
        self._update_rec(a, b, x, 0, 0, self.n)

    def _update_rec(self, a, b, x, k, l, r):
        self.eval(k)
        if r <= a or b <= l:
            return
        elif a <= l and r <= b:
            self.lazy[k] = x
            self.eval(k)
        else:
            self._update_rec(a, b, x, k * 2 + 1, l, (l + r) // 2)
            self._update_rec(a, b, x, k * 2 + 2, (l + r) // 2, r)
            self.elements[k] = max(self.elements[k * 2 + 1], self.elements[k * 2 + 2])


import gc


class LinkedList:
    class Cell:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self, *args):
        self.nil = LinkedList.Cell(None)
        self.nil.next = self.nil
        for x in reversed(args):
            self.insert(x)

    def __del__(self):
        self.nil.next = None

    def _nth(self, n):
        i = -1
        cp = self.top
        while cp is not None:
            if i == n:
                return cp
            i += 1
            cp = cp.link
        return None

    def at(self, n):
        cp = self._nth(n)
        if cp is not None:
            return cp.data
        return None

    def insert(self, v, p=None):
        if p is None:
            p = self.nil
        v.next = p.next
        p.next = v

    def push(self, value):
        data = LinkedList.Cell(value)
        self.insert(data)

    def print_list(self):
        cur = self.nil.next
        while cur != self.nil:
            print(cur.data, "-> ", end="")
            cur = cur.next
        print("")


def change_base(value: int, base: int):
    if int(value / base):
        return change_base(int(value / base), base) + str(value % base)
    return str(value % base)


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


class Binominal:
    def __init__(self, N, mod) -> None:
        fact = [1, 1]
        factinv = [1, 1]
        inv = [0, 1]

        for i in range(2, N + 1):
            fact.append((fact[-1] * i) % mod)
            inv.append((-inv[mod % i] * (mod // i)) % mod)
            factinv.append((factinv[-1] * inv[-1]) % mod)

        self.fact = fact
        self.factinv = factinv
        self.inv = inv
        self.mod = mod
        self.N = N

    def calc(self, n, r):
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.mod


if __name__ == "__main__":
    linkedlist = LinkedList()

    names = ["satoshi", "kakeru", "sho", "kiyoshi", "goro"]

    for name in names:
        linkedlist.push(name)

    linkedlist.print_list()
    del linkedlist
