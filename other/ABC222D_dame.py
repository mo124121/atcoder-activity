N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
MOD = 998244353
ret = 1
for i in range(N):
    ret *= b[i] - a[i] + 1
    ret %= MOD

print(ret)
