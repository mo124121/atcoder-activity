from itertools import permutations


N, M, R = map(int, input().split())
r = list(map(int, input().split()))
INF = 10**18
wf = [[INF] * (N) for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    wf[a][b] = c
    wf[b][a] = c


for k in range(N):
    for i in range(N):
        for j in range(N):
            wf[i][j] = min(wf[i][j], wf[i][k] + wf[k][j])

ret = INF
for pat in permutations(r):
    a = 0
    for i in range(R - 1):
        a += wf[pat[i] - 1][pat[i + 1] - 1]
    ret = min(ret, a)
print(ret)
