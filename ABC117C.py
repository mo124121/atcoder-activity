N, M = map(int, input().split())
X = list(map(int, input().split()))

if N >= M:
    print(0)
    exit()

X.sort()
diff = [X[i + 1] - X[i] for i in range(M - 1)]
diff.sort()
ret = 0
for i in range(M - N):
    ret += diff[i]

print(ret)
