N, P = map(int, input().split())
MOD = 10 ** 9 + 7

ret = pow(P - 2, N - 1, MOD)
ret *= P - 1
ret %= MOD
print(ret)
