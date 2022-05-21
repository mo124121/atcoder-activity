import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")


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


def tousa_sum(a, d, n):
    # 初項a,交差d,項数n
    return n * (2 * a + (n - 1) * d) // 2


# パスカル modなし　O(N**2)
class Binominal:
    def __init__(self, N):
        c = [[0] * (N + 1) for _ in range(N + 1)]

        c[0][0] = 1
        for i in range(N):
            for j in range(i + 1):
                c[i + 1][j] += c[i][j]
                c[i + 1][j + 1] += c[i][j]
        self.c = c

    def calc(self, n, r):
        if r < 0 or n < r:
            return 0
        return self.c[n][r]


# 高速なの　O(N)
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


# nがでかいもの
class Binominal:
    def __init__(self, N, MAX_K, MOD):
        fact_inv = [1, 1]
        inv = [0, 1]
        for i in range(2, MAX_K + 1):
            inv.append((MOD - inv[MOD % i] * (MOD // i)) % MOD)
            fact_inv.append((fact_inv[-1] * inv[-1]) % MOD)
        com = [1]
        for i in range(1, MAX_K + 1):
            com.append((com[-1] * ((N - i + 1) * inv[i] % MOD)) % MOD)
        self.com = com

    def calc(self, k):
        return self.com[k]


# 直接
def comb(n, r, MOD):
    r = min(r, n - r)
    if n == 0:
        return 1
    big = 1
    small = 1
    for i in range(1, r + 1):
        big *= n + 1 - i
        small *= i
    return big // small % MOD


def compress(L):
    S = sorted(set(L))
    d = dict()
    i = 0
    for s in S:
        d[s] = i
        i += 1
    return i, S, d


n, S, d = compress(L)


if __name__ == "__main__":
    linkedlist = LinkedList()

    names = ["satoshi", "kakeru", "sho", "kiyoshi", "goro"]

    for name in names:
        linkedlist.push(name)

    linkedlist.print_list()
    del linkedlist
