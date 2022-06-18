N = int(input())
X = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

seen = set()
ans = 0
for i in range(1, N + 1):
    if i in seen:
        continue
    node = i
    current = set()
    while node not in seen and node not in current:
        current.add(node)
        node = X[node]
    if node in seen:
        seen.update(current)
        continue
    seen.update(current)
    s = X[node]
    r = C[node]
    while s != node:
        r = min(C[s], r)
        s = X[s]
    ans += r

print(ans)
