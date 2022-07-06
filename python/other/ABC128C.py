N, M = map(int, input().split())
s = [list(map(int, input().split()))[1:] for _ in range(M)]
p = list(map(int, input().split()))

from itertools import product

ret = 0
for pat in product([0, 1], repeat=N):
    flag = True
    for i in range(M):
        temp = 0
        for con in s[i]:
            temp += pat[con - 1]
        if temp % 2 != p[i]:
            flag = False
            break
    if flag:
        ret += 1

print(ret)
