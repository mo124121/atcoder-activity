from collections import deque


N = int(input())
S = input()

dq = deque()
for i, c in enumerate(S):
    if len(dq) == 0:
        dq.append(c)
        continue
    elif len(dq) == 1:
        left = dq.popleft()
        if left != c:
            dq.append(c)
            dq.appendleft(left)
        continue
    left = dq.popleft()
    right = dq.pop()
    if left == c:
        dq.append(right)
    elif right == c:
        dq.appendleft(left)
    else:
        dq.appendleft(left)
        dq.append(right)
        if i + 1 < N and S[i + 1] == left:
            dq.append(c)
        else:
            dq.appendleft(c)


print(len(dq))
