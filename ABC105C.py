N = int(input())

v = 4
com_sum = [1, -2]
for i in range(40):
    com_sum.append(v + com_sum[-2])
    v *= -2

if N == 0:
    print(0)
    exit()
elif N > 0:
    i = 0
    while N > com_sum[i]:
        i += 2
else:
    i = 1
    while N < com_sum[i]:
        i += 2

max_i = i


ret = []


def rec(v, i):
    if i < 0:
        return
    if v == 0:
        ret.extend(["0"] * i)
        return
    if v * ((-2) ** i) > 0:
        if abs(v) > abs(com_sum[i - 2]):
            ret.append("1")
            rec(v - (-2) ** i, i - 1)
    else:
        ret.append("0")
        rec(v, i - 1)


rec(N, max_i)

print(*ret, sep="")
