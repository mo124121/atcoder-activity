from collections import Counter
from heapq import heapify, heappop, heappush


def no():
    print("No")
    exit()


H, W = map(int, input().split())

A = [input() for _ in range(H)]
count = Counter()
for a in A:
    for c in a:
        count[c] += 1

ret = [[""] * W for _ in range(H)]

hp = [(-v, k) for k, v in count.items()]
heapify(hp)

for h in range(H // 2):
    for w in range(W // 2):
        count, c = heappop(hp)
        count *= -1
        if count < 4:
            no()
        for x, y in [(h, w), (h, -1 - w), (-1 - h, w), (-1 - h, -1 - w)]:
            ret[x][y] = c
        if count > 4:
            heappush(hp, (4 - count, c))

if H % 2 == 1:
    h = H // 2
    for w in range(W // 2):
        count, c = heappop(hp)
        count *= -1
        if count < 2:
            no()
        for x, y in [(h, w), (h, -1 - w)]:
            ret[x][y] = c
        if count > 2:
            heappush(hp, (2 - count, c))
if W % 2 == 1:
    w = W // 2
    for h in range(H // 2):
        count, c = heappop(hp)
        count *= -1
        if count < 2:
            no()
        for x, y in [
            (h, w),
            (-1 - h, w),
        ]:
            ret[x][y] = c
        if count > 2:
            heappush(hp, (2 - count, c))

if W % 2 == 1 and H % 2 == 1:
    count, c = heappop(hp)
    ret[H // 2][W // 2] = c

print("Yes")


"""
2次元回文
たぶんカウントだけしておけばいい
形状によって変わるのがややこしいが、
4の倍数・2の倍数・残り、みたいな感じになるはず


偶数×偶数


奇数×偶数


奇数×奇数


heap突っ込むか

"""
