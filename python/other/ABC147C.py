from itertools import product


N = int(input())
A = []
for i in range(N):
    c = int(input())
    a = []
    for j in range(c):
        x, y = map(int, input().split())
        x -= 1
        y = bool(y)
        a.append([x, y])
    A.append(a)
ret = 0
for pat in product([True, False], repeat=N):
    flag = True

    for i, a in enumerate(A):
        if not pat[i]:
            continue
        for x, y in A[i]:
            if pat[x] != y:
                flag = False
                break

    count = 0
    for p in pat:
        if p:
            count += 1
    if flag:
        ret = max(ret, count)
print(ret)

"""
N<15
bit全探索 条件にあうかどうかを探す
入力考えるのがだるい
"""
