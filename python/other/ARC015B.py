ret = [0] * 6

N = int(input())
for _ in range(N):
    a, b = map(float, input().split())
    if a >= 35:
        ret[0] += 1
    if 30 <= a < 35:
        ret[1] += 1
    if 25 <= a < 30:
        ret[2] += 1
    if 25 <= b:
        ret[3] += 1
    if b < 0 and 0 <= a:
        ret[4] += 1
    if a < 0:
        ret[5] += 1

print(*ret)
