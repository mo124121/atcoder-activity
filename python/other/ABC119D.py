from bisect import bisect


A, B, Q = map(int, input().split())
INF = 10**18
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
s = [-INF] + s + [INF]
t = [-INF] + t + [INF]

for i in range(Q):
    x = int(input())
    si = bisect(s, x)
    ti = bisect(t, x)
    r = [
        abs(min(s[si - 1], t[ti - 1]) - x),
        abs(max(s[si], t[ti]) - x),
        2 * abs(s[si - 1] - x) + abs(t[ti] - x),
        2 * abs(s[si] - x) + abs(t[ti - 1] - x),
        2 * abs(t[ti - 1] - x) + abs(s[si] - x),
        2 * abs(t[ti] - x) + abs(s[si - 1] - x),
    ]
    print(min(r))
