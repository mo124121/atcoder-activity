MOD = 1000000007
N = int(input())
S = [input() for _ in range(2)]

ret = 1
i = 0
H = 0
V = 1
T = []
while i < N:
    if S[0][i] == S[1][i]:
        T.append(V)
        i += 1
    else:
        T.append(H)
        i += 2

if T[0] == V:
    ret *= 3
    i += 1
    prev = V
else:
    ret *= 6
    i += 2
    prev = H
pat = {(V, V): 2, (V, H): 2, (H, H): 3, (H, V): 1}
for i in range(1, len(T)):
    ret *= pat[(T[i - 1], T[i])]
    ret %= MOD
print(ret)

"""
アルファベットで与えられるぐらいにドミノ数は少ない
2文字連続はややこしい,1文字に圧縮したい

各遷移におけるパターン増加 v縦h横
初期
-> v 3色
-> h 3*2色
継続
v->v 2色
v->h 2色
h->h 2+1色
h->v 1色

"""
