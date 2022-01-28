K = int(input())

from collections import deque

h = list(range(1, 10))
q = deque(h)
count = 0
while True:
    tmp = q.popleft()
    count += 1
    if count == K:
        print(tmp)
        exit()
    digit = tmp % 10
    if digit == 0:
        q.append(tmp * 10 + digit)
        q.append(tmp * 10 + digit + 1)
    elif digit == 9:
        q.append(tmp * 10 + digit - 1)
        q.append(tmp * 10 + digit)
    else:
        q.append(tmp * 10 + digit - 1)
        q.append(tmp * 10 + digit)
        q.append(tmp * 10 + digit + 1)
