from collections import deque


N = int(input())
A = list(map(int, input().split()))

A = deque(A)

ret = 0
l_count = 0
while len(A) > 2:
    l = A[0]
    r = A[-1]
    if l < r:
        A.appendleft(1 + A.popleft() + A.popleft())
        ret += l
        l_count += 1
    else:
        A.append(1 + A.pop() + A.pop())
        ret += r
if l_count % 2:
    ret += A[0]
else:
    ret += A[-1]
print(ret)
