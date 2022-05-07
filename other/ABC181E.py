from bisect import bisect


N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))
H.sort()

L = [0] * (N // 2 + 1)
R = [0] * (N // 2 + 1)

for i in range(0, N - 1, 2):
    L[i // 2 + 1] = L[i // 2] + abs(H[i] - H[i + 1])

for i in range(N - 1, 0, -2):
    R[i // 2 - 1] = R[i // 2] + abs(H[i] - H[i - 1])

ret = 10**9

for w in W:
    i = bisect(H, w)
    r = L[i // 2] + R[i // 2]
    if i % 2 == 0:
        r += abs(w - H[i])
    else:
        r += abs(w - H[i - 1])
    ret = min(ret, r)
print(ret)

"""
過去に解こうとしておいてあった

ソートして
左から偶数の差、右から奇数の差を計算
先生の身長を動かして、bisectしてretを更新

"""
