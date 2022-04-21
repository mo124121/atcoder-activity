N = int(input())
D = list(map(int, input().split()))
MOD = 998244353

d_count = [0] * N

if D[0] > 0:
    print(0)
    exit()

for d in D:
    d_count[d] += 1

if d_count[0] != 1:
    print(0)
    exit()

ret = 1
for i in range(1, N):
    ret *= pow(d_count[i - 1], d_count[i], MOD)
    ret %= MOD
print(ret)

"""
辺の定義での回答なので順番の違いはなさそう

N<10**5

1を頂点とした木として解釈する
距離ごとに個数をカウントして、それぞれがどの親に紐づくのかがパターン数？

in3がWA
何か考慮が足りていない

WA8/RE1
WA8

わからん

解説後
方向は間違っていない
なぜCounterなら行けるのかわからん

単にコーナーケースの考慮不足

"""
