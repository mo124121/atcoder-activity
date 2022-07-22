from itertools import accumulate


N, C = map(int, input().split())
RANGE = 10**5
used = [[0] * (RANGE + 1) for _ in range(C + 1)]

for i in range(N):
    s, t, c = map(int, input().split())
    used[c][s - 1] += 1
    used[c][t] -= 1

for c in range(C + 1):
    for i in range(RANGE):
        used[c][i + 1] += used[c][i]

ret = 0
for i in range(RANGE):
    r = 0
    for c in range(C + 1):
        r += min(1, used[c][i])
    ret = max(ret, r)

print(ret)


"""
自力AC
自分の解法は区間スケジューリングの応用
解説は全部imosっぽい

imosでも実装してみる
"""
