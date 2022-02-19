N = int(input())
A = list(map(int, input().split()))

K = 30

X = A + [0]
sums = [0] * len(X)

for k in range(K):
    ones = []
    for x in X:
        ones.append(x >> k & 1)
    x1 = sum(ones)
    x0 = N - x1

    for i in range(len(ones)):
        sums[i] += (x1 - (x1 - x0) * ones[i]) << k

ANS = max(sums)
print(ANS)
