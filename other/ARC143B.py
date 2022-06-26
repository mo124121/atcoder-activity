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

    def binominal(self, n, r):
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.mod


from itertools import permutations


def solve(N):
    if N == 0:
        return 0

    MOD = 998244353
    bn = Binominal(N**2, MOD)
    r = 1
    r = r * bn.fact[N - 1] % MOD
    r = r * bn.fact[N - 1] % MOD
    r = r * bn.fact[(N - 1) ** 2] % MOD
    r = r * bn.binominal(N**2, 2 * N - 1) % MOD
    r = r * N**2 % MOD

    ret = (bn.fact[N**2] - r) % MOD
    return ret


def main():
    N = int(input())
    print(solve(N))


main()


def naive(N):
    grid = [[0] * N for _ in range(N)]
    ret = 0
    for pat in permutations(range(1, N**2 + 1)):
        for i, p in enumerate(pat):
            grid[i // N][i % N] = p
        flag = True
        for h in range(N):
            for w in range(N):
                vmin = vmax = grid[h][w]
                for hn in range(N):
                    vmax = max(vmax, grid[hn][w])
                for wn in range(N):
                    vmin = min(vmin, grid[h][wn])
                if vmin == vmax:
                    flag = False
                    break
        if flag:
            for g in grid:
                print(*g)
            print()
            ret += 1
    return ret


print(solve(2))
