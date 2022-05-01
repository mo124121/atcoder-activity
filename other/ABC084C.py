N = int(input())
ret = [0] * (N)

for st in range(N - 1):
    C, S, F = map(int, input().split())

    for i in range(st + 1):
        if ret[i] <= S:
            ret[i] = S
        elif ret[i] % F != 0:
            ret[i] = ret[i] - ret[i] % F + F
        ret[i] += C

print(*ret, sep="\n")

"""
普通に愚直にやったらだめ？
あーすべての駅にたいしてやるのか
それでもN<500だしN**2とかN**3ぐらいはできるし余裕では？
都度切り上げた時間から計算していけばいいはず

解説後
S%F==0なのを使ったらもう少しシンプルにはできる

"""
