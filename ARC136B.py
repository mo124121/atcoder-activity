from collections import defaultdict, deque


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

flag = False
q = deque()
seen = defaultdict(int)
for i in range(N):
    q.append(A[i])
    if A[i] in seen:
        flag = True
    seen[A[i]] += 1

total = 0
for i in range(N - 3):
    b = B[i]
    if seen[b] == 0:
        print("No")
        exit()
    seen[b] -= 1
    bufs = []
    while len(q):
        v = q.popleft()
        if v == b:
            if len(bufs):
                dist = len(bufs)
                for j in range(dist - 2):
                    q.appendleft(bufs.pop())
                if len(bufs) == 2:
                    if dist % 2 == 0:
                        q.appendleft(bufs[1])
                        q.appendleft(bufs[0])
                    else:
                        q.appendleft(bufs[0])
                        q.appendleft(bufs[1])
                else:
                    tmp = q.popleft()
                    q.appendleft(bufs[0])
                    q.appendleft(tmp)
            break
        else:
            bufs.append(v)

if len(q) != 3:
    print("No")
    exit()

buf = []
for i in range(3):
    buf.append(q.popleft())
    b = B[-3 + i]
    if seen[b] == 0:
        print("No")
        exit()
    seen[b] -= 1

for i in range(3):
    if (
        buf[(0 + i) % 3] == B[-3]
        and buf[(1 + i) % 3] == B[-2]
        and buf[(2 + i) % 3] == B[-1]
    ):
        flag = True

if flag:
    print("Yes")
else:
    print("No")
