from itertools import combinations

# https://py3.hateblo.jp/entry/2014/02/23/172305
def get_circle_center_and_radius(x1, y1, x2, y2, x3, y3):
    """
    3点を通る円の中心と半径を取得
    """
    d = 2 * ((y1 - y3) * (x1 - x2) - (y1 - y2) * (x1 - x3))
    x = (
        (y1 - y3) * (y1**2 - y2**2 + x1**2 - x2**2)
        - (y1 - y2) * (y1**2 - y3**2 + x1**2 - x3**2)
    ) / d
    y = (
        (x1 - x3) * (x1**2 - x2**2 + y1**2 - y2**2)
        - (x1 - x2) * (x1**2 - x3**2 + y1**2 - y3**2)
    ) / -d
    r2 = (x - x1) ** 2 + (y - y1) ** 2
    return x, y, r2


N = int(input())
x = [0] * N
y = [0] * N

for i in range(N):
    x[i], y[i] = map(int, input().split())

if N <= 2:
    print("{:.7f}".format(((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2) ** 0.5 / 2))
    exit()

r2_min = 1000**3
for c in combinations(range(N), 3):
    x1, y1, x2, y2, x3, y3 = x[c[0]], y[c[0]], x[c[1]], y[c[1]], x[c[2]], y[c[2]]
    x_c, y_c, r2 = get_circle_center_and_radius(x1, y1, x2, y2, x3, y3)
    flag = True
    for i in range(N):
        if i not in c:  # 誤差が怖いので飛ばす
            if (x[i] - x_c) ** 2 + (y[i] - y_c) ** 2 > r2:
                flag = False
                break
    if flag:
        r2_min = min(r2_min, r2)

print("{:.7f}".format(r2**0.5))
