from bisect import bisect, bisect_left


N = int(input())
M = 10**6
A = list(range(2, M + 1))
primes = list()
while A[0] ** 2 <= M:
    tmp = A[0]
    primes.append(tmp)
    A = [e for e in A if e % tmp != 0]
primes += A

ret = 0
for i, q in enumerate(primes):
    if i == 0:
        continue
    r = min(i, bisect(primes, N // (q**3)))
    ret += r
print(ret)


"""
素数列挙して全探索？
Nを超えそうなら枝切り
q**3なので10**6まででいいはず
"""
