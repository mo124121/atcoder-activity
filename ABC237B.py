H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [[0] * H for _ in range(W)]
for i in range(W):
    for j in range(H):
        B[i][j] = A[j][i]

for b_line in B:
    print(*b_line)
