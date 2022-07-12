from typing import Counter


N, D = map(int, input().split())
X, Y = map(int, input().split())

if X % D != 0 or Y % D != 0:
    print(0)
    exit()

X //= D
Y //= D

dp = Counter()
dp[(0, 0)] = 1
for i in range(N):
    nxt = Counter()
    for (x, y), v in dp.items():
        for xm, ym in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            xn = x + xm
            yn = y + ym
            nxt[(xn, yn)] += v / 4
    dp = nxt
print(f"{dp[(X,Y)]:.10f}")
