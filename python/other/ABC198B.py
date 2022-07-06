from collections import deque

N = int(input())
q = deque(list(str(N)))
while len(q) > 0:
    s = q.pop()
    if s != "0":
        q.append(s)
        break


while len(q) > 1:
    l = q.popleft()
    r = q.pop()
    if r != l:
        q.appendleft(l)
        q.append(r)
        break

if len(q) > 1:
    print("No")
else:
    print("Yes")
