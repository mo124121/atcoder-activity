from itertools import product


N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]


ret = -(10**10)
for pat in product((False, True), repeat=10):
    r = 0
    if True not in pat:
        continue
    for j in range(N):
        c = 0
        for i, p in enumerate(pat):
            if p and F[j][i]:
                c += 1
        r += P[j][c]
    ret = max(ret, r)

print(ret)
