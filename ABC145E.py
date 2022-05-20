def solve(N, T, AB):
    dp = [[-1] * (T + 1) for _ in range(N + 1)]
    for i, (a, b) in enumerate(AB):
        dp[i][0] = 0
        for t in range(T):
            if dp[i][t] < 0:
                continue
            nt = min(T, t + a)
            dp[i + 1][t] = max(dp[i + 1][t], dp[i][t])
            dp[i + 1][nt] = max(dp[i + 1][nt], dp[i][nt], dp[i][t] + b)

    return max(dp[N])


def submit():
    N, T = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(tuple(map(int, input().split())))
    AB.sort()
    print(solve(N, T, AB))


submit()

from collections import defaultdict
from itertools import product


def naive(N, T, AB):
    ret = 0
    for pat in product((True, False), repeat=N):
        t = 0
        s = 0
        for i, p in enumerate(pat):
            if p:
                t += AB[i][0]
                s += AB[i][1]
            if AB[i][0] >= T:
                break
        ret = max(ret, s)
    return ret


# import random

# N = 10
# T = 300

# e = 0
# tot = 100
# for t in range(tot):
#     AB = []
#     for i in range(N):
#         AB.append((random.randint(1, 3000), random.randint(1, 300)))

#     s = solve(N, T, AB)
#     g = naive(N, T, AB)
#     if s != g:
#         print("ERROR", t, s, g)
#         print(N, T)
#         for ab in AB:
#             print(*ab)
#         e += 1
# print(f"{e}/{tot}")


"""
見るからにDP
ただ、最後の条件がちょっとやらしい
まあTのところにまとめたらいっか
dp[i][t]:i個目の料理をためべて時刻tの時のスコアの最大値
"""
