from collections import defaultdict


N = int(input())
xy = []
xy_dict = defaultdict(list)
yx_dict = defaultdict(list)
xyd = {}
for i in range(N):
    x, y = map(int, input().split())
    xy.append((x, y))
    xy_dict[x].append(y)
    yx_dict[y].append(x)
    xyd[(x, y)] = True
xy.sort()
ret = 0
for x1, y1 in xy:
    for x2 in yx_dict[y1]:
        if x2 > x1:
            for y2 in xy_dict[x1]:
                if y2 > y1 and (x2, y2) in xyd:
                    ret += 1


print(ret)
