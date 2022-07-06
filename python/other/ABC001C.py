from decimal import ROUND_HALF_UP, Decimal


Deg, Dis = map(int, input().split())
d = "N"
if 1687.5 <= Deg < 1912.5:
    d = "S"
if 112.5 <= Deg < 337.5:
    d = "NNE"
if 1912.5 <= Deg < 2137.5:
    d = "SSW"
if 337.5 <= Deg < 562.5:
    d = "NE"
if 2137.5 <= Deg < 2362.5:
    d = "SW"
if 562.5 <= Deg < 787.5:
    d = "ENE"
if 2362.5 <= Deg < 2587.5:
    d = "WSW"
if 787.5 <= Deg < 1012.5:
    d = "E"
if 2587.5 <= Deg < 2812.5:
    d = "W"
if 1012.5 <= Deg < 1237.5:
    d = "ESE"
if 2812.5 <= Deg < 3037.5:
    d = "WNW"
if 1237.5 <= Deg < 1462.5:
    d = "SE"
if 3037.5 <= Deg < 3262.5:
    d = "NW"
if 1462.5 <= Deg < 1687.5:
    d = "SSE"
if 3262.5 <= Deg < 3487.5:
    d = "NNW"

Dis *= 10 / 60
Dis = Decimal(Dis).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
if 0 <= Dis <= 2:
    w = 0
    d = "C"
if 80 <= Dis <= 107:
    w = 5
if 245 <= Dis <= 284:
    w = 10
if 3 <= Dis <= 15:
    w = 1
if 108 <= Dis <= 138:
    w = 6
if 285 <= Dis <= 326:
    w = 11
if 16 <= Dis <= 33:
    w = 2
if 139 <= Dis <= 171:
    w = 7
if 327 <= Dis:
    w = 12
if 34 <= Dis <= 54:
    w = 3
if 172 <= Dis <= 207:
    w = 8
if 55 <= Dis <= 79:
    w = 4
if 208 <= Dis <= 244:
    w = 9

print(d, w)
