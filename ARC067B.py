N, A, B = map(int, input().split())
X = list(map(int, input().split()))

ret = 0
for i in range(1, N):
    ret += min((X[i] - X[i - 1]) * A, B)

print(ret)
