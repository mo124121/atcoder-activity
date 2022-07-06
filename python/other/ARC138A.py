from bisect import bisect_left, bisect_right
from collections import defaultdict


N, K = map(int, input().split())
A = list(map(int, input().split()))

INF = 10**10

B = A[:K]
B = B[::-1]
C = A[K:]
origin_pos = defaultdict(lambda: int(INF))

for i, c in enumerate(C):
    origin_pos[c] = min(origin_pos[c], i)


C.sort()

k = INF
for c in reversed(C):
    k = min(k, origin_pos[c])
    origin_pos[c] = k

ret = INF
for i, b in enumerate(B):
    j = bisect_right(C, b)
    if j < N - K:
        ret = min(ret, i + origin_pos[C[j]] + 1)
if ret == INF:
    print(-1)
else:
    print(ret)
"""
考察
N<4*10**5
なんか中途半端…3秒だから？

ダメな場合の条件min(A[:K])>max(A[K:])

いい場合、
kまでのやつ一つ一つから、最短で逆転できるやつまでの距離を算出

何とかしてソートしたい
ソート前後の位置変動を知りたい
片方だけでもソートでき、位置がわかれば
bisectでソート後距離-元との変動みたいな感じで出せるはず

別にキーで保存しといたらいい

6/36 WA
どういう戦略で行くか？おそらくちょっとの間違い、抜けているコーナーケースがある

次の大きいやつよりも速く来る奴がある


"""
