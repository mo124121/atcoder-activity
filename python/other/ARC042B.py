x, y = map(int, input().split())
N = int(input())

X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
d = 10**18
for i in range(N):
    xi, yi = X[i], Y[i]
    xj, yj = X[(i + 1) % N], Y[(i + 1) % N]

    a, b, c = (yj - yi), -(xj - xi), yi * (xj - xi) - xi * (yj - yi)
    d = min(d, abs(a * x + b * y + c) / (a**2 + b**2) ** 0.5)

print("{:.6f}".format(d))


"""
蟻本やんけ！->1匹だし違いますね

点と直線の距離ですね

AC
2点を通る1次関数の標準系と、点と直線の距離で説いたが、
解説の原点に直すほうが楽そう

"""
