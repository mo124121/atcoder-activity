from collections import defaultdict
from itertools import product


def greed(N, T, A, B):
    ret = 0
    for pat in product((True, False), repeat=N):
        t = 0
        s = 0
        for i, p in enumerate(pat):
            if p:
                t += A[i]
                s += B[i]
        if t <= T:
            ret = max(ret, s)
    return ret


def solve(N, T, AB):

    seen = defaultdict(int)
    seen[0] = 0
    exceed = defaultdict(int)
    for a, b in AB:
        tmp = defaultdict(int)
        for t, v in seen.items():
            tmp[a + t] = b + v
        for k, v in tmp.items():
            if k < T:
                if seen[k] < v:
                    seen[k] = v
            else:
                if exceed[k] < v:
                    exceed[k] = v
    return max(*seen.values(), *exceed.values())


def submit():
    N, T = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(tuple(map(int, input().split())))
    AB.sort()
    print(solve(N, T, AB))


# submit()

import random

N = 10
T = 300
for t in range(10):
    A = []
    B = []
    for i in range(N):
        A.append(random.randint(1, 3000))
        B.append(random.randint(1, 3000))

    s = solve(N, T, A, B)
    g = greed(N, T, A, B)
    if s != g:
        print(t, s, g)
        print(N, T)
        for a, b in zip(A, B):
            print(a, b)


"""
見るからにDP
ただ、最後の条件がちょっとやらしい
まあTのところにまとめたらいっか
dp[i][t]:i個目の料理をためべて時刻tの時のスコアの最大値
"""
