N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 998244353
rest = sum(A[1:])

if rest + K > A[0]:
    print(0)
    exit()

A[0] -= rest + K


def comb(n, r):
    r = min(r, n - r)
    if n == 0:
        return 1
    big = 1
    small = 1
    for i in range(1, r + 1):
        big *= n + 1 - i
        small *= i
    return big // small % MOD


ret = 1
for i in range(N):
    ret *= comb(A[i] + K - 1, K - 1)
    ret %= MOD

print(ret)
