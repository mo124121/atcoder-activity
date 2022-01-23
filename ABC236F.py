N = int(input())
c = list(map(int, input().split()))

C = [[c[i], i + 1] for i in range(len(c))]
C.sort()

S = []
ret = 0
for c_i, i in C:
    for s in S:
        i = min(i, i ^ s)
    if i != 0:
        S.append(i)
        ret += c_i

print(ret)
