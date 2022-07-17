N, K = map(int, input().split())

dp = set()
dp.add(0)

for i in range(N):
    nxt = set()
    T = list(map(int, input().split()))
    for v in dp:
        for t in T:
            nxt.add(t ^ v)
    dp = nxt
if 0 in nxt:
    print("Found")
else:
    print("Nothing")
