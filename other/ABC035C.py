N, Q = map(int, input().split())
imos = [0] * (N + 1)
for i in range(Q):
    l, r = map(int, input().split())
    imos[l - 1] += 1
    imos[r] -= 1

for i in range(1, N + 1):
    imos[i] += imos[i - 1]

ret = [0] * N
for i in range(N):
    ret[i] = imos[i] % 2

print(*ret, sep="")

"""
都度全部反転していくと間に合わないパターン
いもす
"""
