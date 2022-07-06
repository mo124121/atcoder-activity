N, X = map(int, input().split())
AB = []
for _ in range(N):
    AB.append(list(map(int, input().split())))

ret = 10**19
cum = 0
for i, (a, b) in enumerate(AB):
    cum += a + b
    ret = min(ret, cum + b * max(0, X - i - 1))
print(ret)
