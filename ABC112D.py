N, M = map(int, input().split())
ret = 1
for i in range(1, 10**6 + 1):
    if M % i == 0:
        if M // i >= N:
            ret = max(ret, i)
        if M // (M // i) >= N:
            ret = max(ret, M // i)

print(ret)
