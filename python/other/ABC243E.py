N, M = map(int, input().split())
INF = 10**18
wf = [[INF] * N for _ in range(N)]
G = []
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    wf[a][b] = c
    wf[b][a] = c
    G.append((a, b, c))

for k in range(N):
    for j in range(N):
        for i in range(N):
            wf[i][j] = min(wf[i][j], wf[i][k] + wf[k][j])

ans = 0
for a, b, c in G:
    flag_long = False
    for i in range(N):
        if wf[a][i] + wf[i][b] <= c:
            flag_long = True
    if flag_long:
        ans += 1

print(ans)
