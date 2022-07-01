from collections import Counter

N = int(input())
V = list(map(int, input().split()))
v1 = Counter([v for v in V[::2]])
v2 = Counter([v for v in V[1::2]])
a = v1.most_common(2)
b = v2.most_common(2)

if a[0][0] != b[0][0]:
    print(N - a[0][1] - b[0][1])
else:
    if len(a) == 1:
        a.append((-2, 0))
    if len(b) == 1:
        b.append((-1, 0))
    c = 0
    for ai, i in a:
        for bj, j in b:
            if ai == bj:
                continue
            c = max(c, i + j)
    print(N - c)

"""
一番多いやつに合わせる
2種類にしなければいけないので、
全部同じないしは同じになってしまう場合のケアがいる



"""
