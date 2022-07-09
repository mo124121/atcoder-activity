from math import cos, sin

from numpy import deg2rad


a, b, d = map(int, input().split())

r = deg2rad(d)
x = a * cos(r) - b * sin(r)
y = a * sin(r) + b * cos(r)
print(f"{x:0.7f} {y:0.7f}")
