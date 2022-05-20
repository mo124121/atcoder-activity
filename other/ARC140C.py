N, X = map(int, input().split())

P1 = [1]
diff = 1
i = 2
while i <= N:
    if i == X:
        diff += 1
        i += 1
    P1.append(i)
    diff += 1
    i += diff

P2 = [X]
diff = 1
i = X + diff
while i <= N:
    P2.append(i)
    diff += 1
    i += diff

if len(P1) > len(P2):
    P = P1
else:
    P = P2
seen = set(P)

for i in range(1, N + 1):
    if i not in seen:
        P.append(i)

print(*P)
