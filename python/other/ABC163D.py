N, K = map(int, input().split())
MOD = 10**9 + 7
ret = 0


def f(l, r):
    return (r + l) * (r - l + 1) // 2


for i in range(K, N + 2):
    L = f(0, i - 1)
    R = f(N - i + 1, N)
    ret += R - L + 1
    ret %= MOD

print(ret)


"""
ほほう？

とりあえず個数が違えば値が違うということはわかった

1,4 と 2,3 同じになる

なんかdpっぽいんよね、違うかな

重複するのは選ぶ個数は同じじゃなければいけない


でかい数字がない世界で、Kコ選ぶのはどういうことか
というかそういう問題では？

N<2*10**5

わからんから解説見る



"""
