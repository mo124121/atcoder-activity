N = int(input())

X = [["."] * N for i in range(N)]

for i in range(N):
    for j in range(3):
        X[i][(i * 3 + j) % N] = "#"

if N % 3 != 0:
    X[1], X[N // 3] = X[N // 3], X[1]


for i in range(N):
    ans = "".join(X[i])
    print(ans)
"""
ループするイメージ
N=6はある、すくなくともN%6==0のときは埋められる

問題設定的にN=6~11にあるイメージ
問題はいかにこの基礎解を生成するか？

全探索する？11C3^11 間に合わない
後段に行くほど選択肢は少ない



"""
