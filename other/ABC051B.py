K, S = map(int, input().split())

ret = 0

for x in range(K + 1):
    for y in range(K + 1):
        if 0 <= S - x - y <= K:
            ret += 1

print(ret)
