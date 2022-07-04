N, M = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(N)]

base = B[0][0] - 1
if base % 7 + M > 7:
    print("No")
    exit()
for i in range(N):
    for j in range(M):
        if base + i * 7 + j != B[i][j] - 1:
            print("No")
            exit()
print("Yes")
