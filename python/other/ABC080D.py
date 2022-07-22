N, C = map(int, input().split())

STC = []
for i in range(N):
    s, t, c = map(int, input().split())
    STC.append((t, s, c))
STC.sort()
INF = 10**18
occupied = [0] * C

for t, s, c in STC:
    target = -1
    latest = -1
    for i in range(C):
        if latest < occupied[i] < s:
            target = i
            latest = occupied[i]
    occupied[target] = t

print(len(occupied) - occupied.count(0))


"""
自力AC
自分の解法は区間スケジューリングの応用
解説は全部imosっぽい
"""
