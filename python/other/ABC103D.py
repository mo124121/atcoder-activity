N, M = map(int, input().split())

AB = []
for i in range(M):
    a, b = map(int, input().split())
    AB.append((a, b))
AB.sort()
ret = 0
left = 0
right = 0
for a, b in AB:
    left = max(left, a)
    right = min(right, b)
    if left >= right:
        ret += 1
        left = a
        right = b

print(ret)
