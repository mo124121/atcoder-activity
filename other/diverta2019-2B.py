from collections import deque


N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

ret = 10**10
for x1, y1 in zip(X, Y):
    for x2, y2 in zip(X, Y):
        if (x1, y1) == (x2, y2):
            continue
        p = x2 - x1
        q = y2 - y1

        Q = deque()
        seen = {}
        seen[(x1, y1)] = 0
        Q.append((x2, y2, 1))

        while len(Q):
            x, y, c = Q.popleft()
            if (x, y) in seen:
                continue
            seen[(x, y)] = c
            for nx, ny in zip(X, Y):
                if (nx, ny) in seen or (x, y) == (nx, ny):
                    continue
                if x + p == nx and y + q == ny:
                    Q.appendleft((nx, ny, c))
                else:
                    Q.append((nx, ny, c + 1))
        r = 0
        for c in seen.values():
            r = max(r, c)
        ret = min(ret, r)
print(ret)
"""
Nが小さい
とりあえず全ペアの差が候補
条件を満たす場合はコスト0,満たさない場合はコスト1で遷移できるグラフ問題？
ダイクストラまたは01DFSで探す
"""
