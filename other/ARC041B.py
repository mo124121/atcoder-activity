N, M = map(int, input().split())
A = [[0] * M for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]

for n in range(1, N - 1):
    for m in range(1, M - 1):
        A[n][m] = B[n - 1][m]
    for m in range(1, M - 1):
        B[n][m] -= A[n][m - 1] + A[n - 1][m] + A[n][m + 1]

for a in A:
    print(*a, sep="")
"""
端から貪欲にしておけばよさそう
なんらか漸化式が組めるはず

A
0 0 0 0 0
0 1 2 3 0
0 4 5 6 0
0 7 8 9 0
0 0 0 0 0
B
   0    1    2   3   0
   1   24  135  26   3
   4  157 2468 359   6 
   7   48  579  68   9
   0    7    8   9   0 


"""
