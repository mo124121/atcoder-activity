N, K = map(int, input().split())


def f(a):
    g1 = list(str(a))
    g1.sort(reverse=True)
    g2 = list(str(a))
    g2.sort()
    return int("".join(g1)) - int("".join(g2))


ret = N

for i in range(K):
    ret = f(ret)

print(ret)
