L1, R1, L2, R2 = map(int, input().split())

ret = [0] * 111

for i in range(L1, R1 + 1):
    ret[i] += 1
for i in range(L2, R2 + 1):
    ret[i] += 1

print(max(ret.count(2) - 1, 0))
