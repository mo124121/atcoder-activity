N, X = map(int, input().split())

V = [0] * N
P = [0] * N

for i in range(N):
    V[i], P[i] = map(int, input().split())

q = 0
for i in range(N):
    q += V[i] * P[i]
    if q / 100 > X:
        print(i + 1)
        exit()

print(-1)
