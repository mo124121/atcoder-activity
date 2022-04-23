H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

ret = []
i = 0
l = 0
line = []
d = 1
for i, a in enumerate(A):
    for _ in range(a):
        if len(line) == W:
            ret.append(line[::d])
            line = []
            d *= -1
        line.append(i + 1)

ret.append(line[::d])

for r in ret:
    print(*r)


"""
くねくねしていったら繋がりそう
"""
