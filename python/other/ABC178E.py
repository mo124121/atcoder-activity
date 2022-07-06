N = int(input())
U = []
V = []
for i in range(N):
    x, y = map(int, input().split())
    U.append(x - y)
    V.append(x + y)
print(max(max(U) - min(U), max(V) - min(V)))
