from math import atan2, cos, pi, sin, degrees

N = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
xc, yc = (x1 + x2) / 2, (y1 + y2) / 2
r = (((x1 - x2) / 2) ** 2 + ((y1 - y2) / 2) ** 2) ** 0.5
theta1 = atan2(y1 - yc, x1 - xc)
theta_ret = theta1 + 2 * pi / N
xr = xc + r * cos(theta_ret)
yr = yc + r * sin(theta_ret)

print("{:.7f} {:.7f}".format(xr, yr))

"""
幾何めんどくさい…

直径わかるわけだし、三角関数で求めたらあかんの？

中心((x1+x2)/2, (y1+y2)/2) 半径((x1-x2)/2**2+(y1-y2)/2**2)**.5の円
(x1,y1)から2pi/N角度を進めた位置

"""
