H, W, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) % K != sum(B) % K:
    print(-1)
    exit()

zh = 0
for a in A:
    zh += ((K - 1) - (a - (W - 1) * (K - 1))) % K
zw = 0
for b in B:
    zw += ((K - 1) - (b - (H - 1) * (K - 1))) % K
print(H * W * (K - 1) - max(zh, zw))
