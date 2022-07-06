from collections import Counter


N = int(input())
S = input()
MOD = 10**9 + 7
count = Counter(S)
ret = 1
for v in count.values():
    ret = ret * (v + 1) % MOD
ret -= 1
ret %= MOD
print(ret)

"""
結局取り出す位置が違っていいならなんでもいいのでは・・・？
全て異なる文字、さて

同じ文字は拾ってはいけない
Π(ある文字種の個数+1)-1


"""
