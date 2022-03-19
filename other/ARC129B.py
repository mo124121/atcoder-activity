N = int(input())

L = [] * N
R = [] * N
max_l = 0
min_r = 10**9
ret = []
for i in range(N):
    L, R = map(int, input().split())
    max_l = max(max_l, L)
    min_r = min(min_r, R)
    ret.append(max(0, (max_l - min_r + 1) // 2))

print(*ret, sep="\n")

"""
考察
すごい累積和っぽい？

全探索
都度、すべて合算してminをサーチ　貪欲法？
単調増加じゃないから2分探索は使えなさそう

セグ木っぽくもある


1 3 0
2 4 0
5 6 1

合計じゃなくてmax

一番大きいLと一番小さいRだけ保管しておけばいい？
"""
