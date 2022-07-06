from collections import Counter, defaultdict, deque


N = int(input())

G = defaultdict(list)

for i in range(1, N):
    a, b = map(int, input().split())
    G[a].append((b, i))
    G[b].append((a, i))
ret = [0] * (N)

q = deque()
q.append((1, -1))
seen = set()
seen.add(1)
while len(q):
    node, color = q.popleft()
    color_nxt = 1
    for neibor, i in G[node]:
        if neibor not in seen:
            if color == color_nxt:
                color_nxt += 1
            q.append((neibor, color_nxt))
            seen.add(neibor)
            ret[i] = color_nxt
            color_nxt += 1

print(len(set(ret[1:])))
for i in range(1, N):
    print(ret[i])

"""
普通にやってくだけでは？

最小の色数=子の最大数+親

"""
