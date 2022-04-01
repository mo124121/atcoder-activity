# https://muhenkou.net/?p=7691#%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3
# エラトステネスの篩 O(NloglogN)
N = int(input())
A = list(range(2, N + 1))
p = list()
while A[0] ** 2 <= N:
    tmp = A[0]
    p.append(tmp)
    A = [e for e in A if e % tmp != 0]
print(p + A)

# https://muhenkou.net/?p=7691#%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3
# 素因数分解 O(√N)???
N = int(input())
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
print(list(ans.items()))
