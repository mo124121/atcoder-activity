N = int(input())
MOD = 998244353
ret = 0
for i in range(1, 19):
    if N >= 10 ** i:
        current = (10 ** i - 10 ** (i - 1)) % MOD
        ret += current * (current + 1) // 2
        ret %= MOD
    else:
        current = (N + 1 - 10 ** (i - 1)) % MOD
        ret += current * (current + 1) // 2
        ret %= MOD
        break

print(ret)
