N, M, Q = map(int, input().split())
memo = [[0] * (N) for _ in range(N)]
L = [0] * M
R = [0] * M
for i in range(M):
    L[i], R[i] = map(int, input().split())

for l in range(N - 1):
    for m in range(M):
        if l <= L[m] - 1:
            memo[l][R[m] - 1] += 1
    for r in range(N - 1):
        memo[l][r + 1] += memo[l][r]

ret = []
for _ in range(Q):
    p, q = map(int, input().split())
    ret.append(memo[p - 1][q - 1])

print(*ret, sep="\n")

"""
N<500
M<2*10**5
Q<10**5

NM<10**8　ギリギリくさい　でも3秒あるし・・・？

Nが小さいので、N~Mの範囲の本数数えといたら？
累積和てきなものをとっておくイメージ



"""
