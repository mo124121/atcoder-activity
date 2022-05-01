N, T = map(int, input().split())
tot = 0
Diff = []
for i in range(N):
    a, b = map(int, input().split())
    tot += a
    Diff.append(b - a)

Diff.sort()

if tot <= T:
    print(0)
    exit()
ret = 1
for d in Diff:
    tot += d
    if tot <= T:
        print(ret)
        exit()
    ret += 1
print(-1)
