# https://muhenkou.net/?p=7691#%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3
# ちょい改変
# エラトステネスの篩 O(NloglogN)
N = int(input())
base = list(range(2, N + 1))
primes = list()
while base[0] ** 2 <= N:
    tmp = base[0]
    primes.append(tmp)
    base = [e for e in base if e % tmp != 0]
primes += base
print(primes)


# 　エラトステネスの篩 2
N = 10**5 + 100

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
i = 2
while i**2 <= N:
    if is_prime[i]:
        j = i * 2
        while j <= N:
            is_prime[j] = False
            j += i
    i += 1


# https://muhenkou.net/?p=7691#%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3
# 素因数分解 O(√N)???
N = int(input())


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


ans = prime_factorization(N)
print(list(ans.items()))
