N, L = map(int, input().split())

XD = [[0, "R"]]
for i in range(N):
    x, d = input().split()
    x = int(x)
    XD.append((x, d))
XD.append([L + 1, "L"])

ret = 0
s = 0
t = 0
while s < N + 2:
    r = []
    while XD[t][1] == "R":
        r.append(XD[t][0])
        t += 1
    l = []
    while t < N + 2 and XD[t][1] == "L":
        l.append(XD[t][0])
        t += 1
    d_r = len(r) - int(r[0] == 0)
    d_l = len(l) - int(l[-1] == L + 1)
    if d_r > d_l:
        ret += d_r * (l[0] - r[-1] - 1)
    else:
        ret += d_l * (l[0] - r[-1] - 1)

    for i, ri in enumerate(r[:-1]):
        if ri == 0:
            continue
        ret += r[-1] - ri - (len(r) - 1 - i)

    for i, li in enumerate(l[1:]):
        if li == L + 1:
            continue
        ret += li - l[0] - 1 - i
    s = t

print(ret)
