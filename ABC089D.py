H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

pos = {}
for h in range(H):
    for w in range(W):
        pos[A[h][w]] = (h, w)

csum = [0] * (H * W + 1)
for i in range(1, H * W - D + 1):
    csum[i + D] = (
        csum[i] + abs(pos[i][0] - pos[i + D][0]) + abs(pos[i][1] - pos[i + D][1])
    )

Q = int(input())
ret = []
for _ in range(Q):
    l, r = map(int, input().split())
    ret.append(csum[r] - csum[l])

print(*ret, sep="\n")

"""
Dは同じなので事前に累積和を計算、l,rで差を取る
"""
