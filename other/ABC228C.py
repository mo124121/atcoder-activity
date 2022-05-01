N, K = map(int, input().split())
P = []

for _ in range(N):
    P.append(sum(map(int, input().split())))

Q = P[::]
Q.sort(reverse=True)
target = Q[K - 1]

ret = []
for p in P:
    if target <= p + 300:
        ret.append("Yes")
    else:
        ret.append("No")

print(*ret, sep="\n")
