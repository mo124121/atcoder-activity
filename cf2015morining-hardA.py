from collections import deque


N = int(input())
A = list(map(int, input().split()))
dq = deque()
for i in range(N):
    dq.append((A[i], i % 2))

ret = 0
while len(dq) > 2:
    l, c_l = dq.popleft()
    r, c_r = dq.pop()
    if l <= r:
        ret += l
        m, c_m = dq.popleft()
        l += m + 1
        c_l = c_m
    else:
        ret += r
        m, c_m = dq.pop()
        r += m + 1
        c_r = c_m

    dq.append((r, c_r))
    dq.appendleft((l, c_l))

l, c_l = dq.popleft()
r, c_r = dq.pop()

if c_r == 1:
    ret += r
else:
    ret += l

print(ret)
