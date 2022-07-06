T = int(input())
ret = []
for t in range(T):
    N, M = map(int, input().split())
    XY = []
    for i in range(N):
        XY.append(tuple(map(int, input().split())))
    r = -(10**18)
    A = 0
    Bpre = 0
    for x, y in XY:
        B = Bpre + x * y
        r = max(r, A + Bpre + x)
        if Bpre > 0 and B < 0:
            yi = Bpre // abs(x)
            r = max(r, A + (Bpre + x + Bpre + x * yi) * yi // 2)
        A += y * (Bpre + x + B) // 2
        Bpre = B
    r = max(r, A)

    ret.append(r)

print(*ret, sep="\n")
