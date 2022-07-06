N = int(input())
S = list(map(int, list(input().replace("R", "0").replace("G", "1").replace("B", "2"))))
rgb = [0, 1, 2]
c_l = [[0] * 3 for _ in range(N)]
c_r = [[0] * 3 for _ in range(N)]


for i in range(1, N):
    for j in range(3):
        c_r[-i - 1][j] = c_r[-i][j]
        if S[-i] == j:
            c_r[-i - 1][j] += 1

ret = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        if S[i] != S[j]:
            c_j = 3 - S[i] - S[j]
            ret += c_r[j][c_j]
            if j + (j - i) < N and S[j + (j - i)] == c_j:
                ret -= 1

print(ret)
