N = int(input())
tc, ac = map(int, input().split())
for i in range(N - 1):
    T, A = map(int, input().split())
    n = max((tc + T - 1) // T, (ac + A - 1) // A)
    tc = n * T
    ac = n * A

print(tc + ac)
