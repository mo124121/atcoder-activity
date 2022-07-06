N = int(input())
P = list(map(int, input().split()))
P2 = P.copy()
ret = 0
for i in range(N - 1):
    if i + 1 == P[i]:
        P[i + 1] = i + 1
        ret += 1
    else:
        pass
if P[N - 1] == N:
    ret += 1

ret2 = 0
for i in range(N - 1, 0, -1):
    if i + 1 == P2[i]:
        P2[i - 1] = i + 1
        ret2 += 1
if P[0] == 1:
    ret2 += 1


print(min(ret, ret2))
