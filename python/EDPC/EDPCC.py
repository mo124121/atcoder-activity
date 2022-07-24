N = int(input())
dp = [0] * 3

for i in range(N):
    nxt = [0] * 3
    abc = list(map(int, input().split()))
    for j in range(3):
        nxt[j] = max(dp[(j + 1) % 3] + abc[j], dp[(j + 2) % 3] + abc[j])
    dp = nxt
print(max(dp))
