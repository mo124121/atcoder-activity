from math import pi


l = list(map(int, input().split()))
INF = 10 ** 9
ret = (sum(l)) ** 2 * pi
ret_m = INF
if l[0] > l[1] + l[2]:
    ret_m = (l[0] - l[1] - l[2]) ** 2 * pi

if l[0] + l[1] < l[2]:
    ret_m = min(ret_m, (l[2] - l[1] - l[0]) ** 2 * pi)

if l[1] > l[0] + l[2]:
    ret_m = min(ret_m, (l[1] - l[0] - l[2]) ** 2 * pi)

if ret_m != INF:
    ret -= ret_m
print("{:.7f}".format(ret))
