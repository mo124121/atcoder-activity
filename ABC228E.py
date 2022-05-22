N, K, M = map(int, input().split())
MOD = 998244353
print(int(M % MOD != 0) * pow(M, pow(K, N, MOD - 1), MOD))
