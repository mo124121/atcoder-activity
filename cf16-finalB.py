N = int(input())

total = 0
for i in range(1, N + 1):
    total += i
    if total >= N:
        break

if total == N:
    print(*list(range(1, i + 1)), sep="\n")
    exit()

ret = list(range(1, i))
diff = N - sum(ret)

for i in range(diff):
    ret[-1 - i] += 1

print(*ret, sep="\n")
