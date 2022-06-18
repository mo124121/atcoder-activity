N = int(input())
LR = []
for _ in range(N):
    LR.append(tuple(map(int, input().split())))

LR.sort()

ret = []
for l, r in LR:
    if ret and l <= ret[-1][1]:
        ret[-1][1] = max(r, ret[-1][1])
    else:
        ret.append([l, r])

for l, r in ret:
    print(l, r)


"""
一回あきらめた貪欲法のデバッグ
"""
