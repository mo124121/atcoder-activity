N, D = map(int, input().split())
MOD = 998244353


f = [0] * (N + 1)
g = [0] * (N + 1)

for i in range(1, N + 1):
    l = i - 1
    r = D - l
    leaf = 0
    if 0 <= r <= i - 1:
        leaf = pow(2, l - 1, MOD) * pow(2, max(0, r - 1), MOD)
        if l != r:
            leaf *= 2
        leaf %= MOD
    g[i] = (g[i - 1] + leaf) % MOD

for i in range(1, N + 1):
    f[i] = (f[i - 1] * 2 + g[i]) % MOD

print(f[N] * 2 % MOD)
