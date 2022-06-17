N, X, M = map(int, input().split())
keta = 40

A = [[0] * M for _ in range(keta + 1)]
T = [[0] * M for _ in range(keta + 1)]
for v in range(M):
    A[0][v] = v
    T[0][v] = v * v % M

for i in range(keta):
    for v in range(M):
        A[i + 1][v] = A[i][v] + A[i][T[i][v]]
        T[i + 1][v] = T[i][T[i][v]]
ret = 0
for i in range(keta):
    if (N >> i) & 1:
        ret += A[i][X]
        X = T[i][X]

print(ret)

"""
ダブリングを覚えよ
"""
