N = int(input())

M = "Male"
F = "Female"
V = "Vacant"

l = 0
r = N
print(l, flush=True)
stat_l = input()
if stat_l == V:
    exit()
while True:
    m = (l + r) // 2
    print(m, flush=True)
    stat = input()
    if stat == V:
        break
    if (stat_l == stat) ^ (m % 2 != 0):
        l = m
    else:
        r = m


"""
2分探索的な発想になるはず

m男
f女
v空席

mvm,fvfを探すのはあきらめる
2分探索で上側と下側で挙動が変わるはず

差が2の倍数の時
  状態が同じ->mfmfmで存在なしかも
  状態が違う->mfvmfで存在する
差が2の倍数でない時
　状態が同じ->mfvmで存在する
　状態が違う->mfmfで存在なしかも

桁上がり

両方ともない場合どうするか？

解説
あってはいるはず

うまくいかないので
lを固定して二分探索　そのほうがシンプル

"""
