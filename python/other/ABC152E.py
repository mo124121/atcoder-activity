from collections import Counter


N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7


def prime_factorization(N):
    i = 2
    ans = dict()
    n = N
    while i * i <= N:
        while n % i == 0:
            n = n // i
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        i += 1
    if n != 1:
        ans[n] = 1
    return ans


whole_primes = Counter()
for a in A:
    primes = prime_factorization(a)
    for k, v in primes.items():
        whole_primes[k] = max(whole_primes[k], v)

total_dot = 1
for k, v in whole_primes.items():
    total_dot *= pow(k, v, MOD)
    total_dot %= MOD

ans = 0
for a in A:
    ans += total_dot * pow(a, MOD - 2, MOD) % MOD

print(ans % MOD)
