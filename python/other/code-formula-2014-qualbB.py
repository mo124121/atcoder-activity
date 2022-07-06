N = int(input())
A = [int(input()) for _ in range(N)]


MOD = 1000000007
ret = 1

B = []
tmp = []
scope = 0
for a in A:
    tmp.append(a)
    scope = max(scope - 1, len(str(a)))
    if scope == 1:
        B.append(tmp)
        tmp = []
if tmp:
    B.append(tmp)

ret = 1
for bs in B:
    tmp = 0
    for b in reversed(bs):
        tmp = tmp * 10 + b
        tmp %= MOD
    ret = ret * (tmp + 1) % MOD

print((ret - 1) % MOD)
