N = int(input())
A = list(map(int, input().split()))

As = sum(A)

if As % N != 0:
    print(-1)
    exit()

ave = As // N
B = [A[i] - ave for i in range(N)]

c = B[0]
ret = 0
for b in B[1:]:
    if c != 0:
        ret += 1
    c += b

print(ret)


"""
あまる状況は-1
そうでなければ全部つないだら最悪でもできる

とりあえず平均の個数を引いてシンプルにする

順に見ていって、過去の合計値が0じゃないときだけつなぐ
"""
