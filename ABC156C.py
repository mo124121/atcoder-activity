N = int(input())
X = list(map(int, input().split()))

INF = 10**10

ret = INF

for P in range(1, 101):
    tmp = 0
    for x in X:
        tmp += (x - P) ** 2
    ret = min(ret, tmp)

print(ret)
