from collections import deque


N = int(input())
A = [list(map(int, input().split())) for _ in range(2 * N - 1)]


ret = 0

q = deque()

q.append([0])

while len(q):
    current = q.pop()
    if len(current) == 2 * N:
        tmp = 0
        for i in range(N):
            tmp ^= A[current[i * 2]][current[i * 2 + 1] - current[i * 2] - 1]
        ret = max(ret, tmp)
    elif len(current) % 2 == 1:
        for i in range(2 * N):
            if i not in current:
                q.append(current + [i])
    else:
        for i in range(2 * N):
            if i not in current:
                q.append(current + [i])
                break

print(ret)
