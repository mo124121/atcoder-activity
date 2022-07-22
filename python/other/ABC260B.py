N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
seen = set()
Ai = [(-a, i) for i, a in enumerate(A)]
Ai.sort()
for a, i in Ai:
    if X == 0:
        break
    if i + 1 not in seen:
        seen.add(i + 1)
        X -= 1

Bi = [(-b, i) for i, b in enumerate(B)]
Bi.sort()

for b, i in Bi:
    if Y == 0:
        break
    if i + 1 not in seen:
        seen.add(i + 1)
        Y -= 1

ABi = [(-a - b, i) for i, (a, b) in enumerate(zip(A, B))]
ABi.sort()
for _, i in ABi:
    if Z == 0:
        break
    if i + 1 not in seen:
        seen.add(i + 1)
        Z -= 1

print(*sorted(list(seen)), sep="\n")
