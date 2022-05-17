N, K = map(int, input().split())
S = input() + "#"

L = []
l = -1

for i in range(N):
    if S[i] != S[i + 1]:
        L.append(i - l)
        l = i
ret = 0
for l in L:
    ret += l - 1
while K > 0 and len(L) > 2:
    ret += 2
    L.pop()
    L.pop()
    K -= 1
if len(L) == 2 and K > 0:
    ret += 1
print(ret)

"""
N,K<10**5

LR入り混じりの範囲を反転させても
端以外は値は変わらないはず
結局連続する区間を操作していくイメージ

RLLLR 2
RRRRR 4

RLR 0
RRR 2

ランレングス圧縮してまず個数をカウント
順次反転するごとに+2
両端のカウントは注意 +1

"""
