a, N = map(int, input().split())

x = 1
INF = 10 ** 9


def rotate(num: int):
    s = str(num)
    return int(s[-1] + s[:-1])


seen = {}

from collections import deque


def solve():
    task = deque()
    task.append((1, 0))
    ret = -1
    while len(task):
        x, i = task.popleft()
        if x in seen:
            continue
        else:
            seen[x] = True
        if x == N:
            ret = i
            break
        if len(str(x)) > len(str(N)):
            continue

        task.append((x * a, i + 1))
        if x >= 10 and x % 10 != 0:
            task.append((rotate(x), i + 1))

    print(ret)


solve()
