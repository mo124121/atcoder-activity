N = int(input())
A = list(map(int, input().split()))
ret = [0] * (N + 1)
ret[0] = 0
MOD = 360
for i in range(N):
    ret[i + 1] = (A[i] + ret[i]) % MOD

ret.sort()
ret.append(360)
r = 0
for i in range(len(ret) - 1):
    r = max(r, ret[i + 1] - ret[i])

print(r)
