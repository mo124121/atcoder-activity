N, K = map(int, input().split())
A = list(map(int, input().split()))
logK = 41

doubling = [[0] * N for _ in range(logK + 1)]

for i in range(N):
    doubling[0][i] = A[i]

for k in range(logK):
    for i in range(N):
        doubling[k + 1][i] = doubling[k][i] + doubling[k][(i + doubling[k][i]) % N]

ret = 0
pos = 0
for k in range(logK):
    if (K >> k) & 1:
        ret += doubling[k][pos]
        pos = (pos + doubling[k][pos]) % N
print(pos)


"""
K回の操作の中で、各要素何回出てきますか？という問題
ダンプリングくさい、が実装は忘れた
"""
