T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    B = 0
    A = 0
    ret = -5
    for i in range(N):
        x, y = map(int, input().split())
        if i == 0:
            ret = max(ret, x)
        if B > 0 and x < 0:
            d = B // -x
            if d < y:
                ret = max(ret, A + B * d + x * d * (d + 1) // 2)
        A += B * y + x * y * (y + 1) // 2
        B += x * y
        ret = max(ret, A)

    print(ret)


"""
xiの範囲が小さい
"""
