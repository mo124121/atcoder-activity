from collections import deque


N = int(input())
A = list(map(int, input().split()))

q = deque()
sum = 0
ret = []
for i in range(N):
    a = A[i]
    if len(q) == 0:
        q.append((a, 1))
        sum += 1
    else:
        bef, count = q.pop()
        if a == bef:
            if count + 1 != a:
                q.append((a, count + 1))
                sum += 1
            else:
                sum -= a - 1
        else:
            q.append((bef, count))
            q.append((a, 1))
            sum += 1

    ret.append(sum)

print(*ret, sep="\n")
