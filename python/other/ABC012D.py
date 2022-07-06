N, M = map(int, input().split())
INF = 10**10
T = [[INF] * (N) for _ in range(N)]
for i in range(N):
    T[i][i] = 0
for i in range(M):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    T[a][b] = t
    T[b][a] = t

for k in range(N):
    for i in range(N):
        for j in range(N):
            T[i][j] = min(T[i][j], T[i][k] + T[k][j])

ret = INF
for Ti in T:
    ret = min(ret, max(Ti))
print(ret)
"""
N<=300
N**3はいける N**4は厳しい

とりあえず全ノード間の最短経路を計算し、
あるノードから他のノードへの時間の最大値を算出
もっとも短くなるケースが答え

ワーシャルフロイドですね

AC

"""
