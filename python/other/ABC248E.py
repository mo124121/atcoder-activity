N, K = map(int, input().split())

X = [0] * N
Y = [0] * N

for i in range(N):
    X[i], Y[i] = map(int, input().split())

if K == 1:
    print("Infinity")
    exit()


def on_line(i2, i1, i0):
    return (Y[i2] - Y[i0]) * (X[i1] - X[i0]) == (X[i2] - X[i0]) * (Y[i1] - Y[i0])


lines = {}
ret = 0
seen = {}
for i in range(N - 1):
    for j in range(i + 1, N):
        if (i, j) in seen or (j, i) in seen:
            continue
        c = 2
        ps = [i, j]
        for k in range(j + 1, N):
            if on_line(i, j, k):
                ps.append(k)
                c += 1

        for ii in range(c):
            for jj in range(ii + 1, c):
                seen[ps[ii], ps[jj]] = True
        if c >= K:
            ret += 1


print(ret)

"""
K=1 無限
K=2 引けるすべての線,重複したらNG

これなんかでみたことあるんだよなあ

N<300
N^3までいけそう、逆にN^4は厳しそう

on line -> (y2-y0)/(x2-x0)==(y1-y0)/(x1-x0)
とりあえず全部のペアの直線を出す->グルーピングできるやつを一緒にして削る
削るときは他方の二つ以上の点が自分の線を通ること
通っていたら消していい

とりあえず線候補を傾きあたりでソートして登録
アー水平とかダルイナー

他手法考える
dpとかはどうか？

なんか再帰的になるように見える



"""
