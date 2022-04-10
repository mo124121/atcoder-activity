N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
pair = {}
MOD = 998244353

for i in range(N):
    pair[P[i]] = Q[i]


"""
考察だけでもする

N<10**5
O(NlogN)ぐらい

全部網羅する

裏に数字が書いてある分、とらなくていい選択が増えるイメージ 2倍

最小は1 最大は例えばどの半分をとってもとれるケース N C N//2


解説後
グラフ、という事実だけで考えなおしてみる
わからん



"""
