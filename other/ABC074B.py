N = int(input())
K = int(input())
X = list(map(int, input().split()))

ret = 0

for x in X:
    ret += min(x, K - x) * 2
print(ret)
