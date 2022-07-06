N = int(input())
C = [0] + list(map(int, input().split()))

cmin = min(C[1:])
l = N // cmin

ret = []

for i in range(l):
    for j in range(9, 0, -1):
        if cmin * (l - i - 1) + C[j] <= N:
            N -= C[j]
            ret.append(str(j))

print(*ret, sep="")
