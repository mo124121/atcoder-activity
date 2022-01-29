N, L, W = map(int, input().split())
A = list(map(int, input().split()))
A.append(L)

left = 0
ret = 0
for a in A:
    diff = a - left
    if diff > 0:
        ret += (diff + W - 1) // W
    left = a + W

print(ret)
