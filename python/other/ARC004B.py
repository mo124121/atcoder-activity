N = int(input())
d = [int(input()) for _ in range(N)]
d.sort(reverse=True)
print(sum(d))
print(max(0, d[0] - sum(d[1:])))
