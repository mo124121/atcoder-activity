from collections import deque
from functools import lru_cache


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
pair = {}
MOD = 998244353


@lru_cache(maxsize=None)
def luca(i):
    if i == 1:
        return 2
    if i == 2:
        return 3
    return luca(i - 1) + luca(i - 2)


seen = {}
for i in range(N):
    pair[P[i]] = Q[i]

ls = []
st = list(range(1, N + 1))
ret = 1
while len(st):
    i = st.pop()
    if i in seen:
        continue
    l = 0
    while i not in seen:
        seen[i] = True
        i = pair[i]
        l += 1
    ret *= luca(l)
    ret %= MOD
print(ret)

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
