N = int(input())
LR = []
W = 2 * 10**5
imos = [0] * (W + 1)
for _ in range(N):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r] -= 1

for i in range(W):
    imos[i + 1] += imos[i]

ret = []
for i in range(W):
    if imos[i] == 0 and imos[i + 1] != 0:
        l = i + 1
    if imos[i] != 0 and imos[i + 1] == 0:
        r = i + 1
        ret.append((l, r))

for l, r in ret:
    print(l, r)
