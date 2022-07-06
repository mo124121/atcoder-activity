N, M = map(int, input().split())

INF = 10**18

wf = [[INF] * (N + 1) for _ in range(N + 1)]
cands = []
for i in range(M):
    u, v, w = map(int, input().split())
    if u == 1 or v == 1:
        cands.append((max(u, v), w))
    else:
        wf[u][v] = w
        wf[v][u] = w


for k in range(2, N + 1):
    for i in range(2, N + 1):
        for j in range(2, N + 1):
            wf[i][j] = min(wf[i][j], wf[i][k] + wf[k][j])

ret = INF
for s, ws in cands:
    for t, wt in cands:
        if s != t:
            ret = min(ret, ws + wt + wf[s][t])

if ret == INF:
    print(-1)
else:
    print(ret)


"""
解説後AC 
1を例外として考える
最短閉路は部分的には最短経路ににた性質を持っている
"""
