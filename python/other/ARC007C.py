from collections import deque

C = input().replace("o", "1").replace("x", "0")
N = len(C)
base = int(C, 2)


def shift(pat, i):
    ret = pat >> i
    ret2 = pat << (N - i)
    return (ret2 | ret) & ((1 << N) - 1)


goal = (1 << N) - 1

q = deque()
q.append((base, 1))
seen = set()
seen.add(base)
while len(q):
    p, c = q.popleft()
    if p == goal:
        print(c)
        exit()
    for i in range(1, N):
        nxt = p | shift(base, i)
        if nxt not in seen:
            q.append((nxt, c + 1))
            seen.add(nxt)
"""
DPっぽい
bitシフトしたやつでどれだけ埋められるか、みたいな
bit全探索

64MB制限とかいう…pypyだとMLE
"""
