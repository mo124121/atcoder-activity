D = list(map(int, input().split()))
J = list(map(int, input().split()))

ret = 0
for d, j in zip(D, J):
    ret += max(d, j)

print(ret)
