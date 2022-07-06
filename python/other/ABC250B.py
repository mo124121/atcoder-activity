N, A, B = map(int, input().split())

c = [".", "#"]
line_pos = ""
line_neg = ""
for i in range(N):
    line_pos += c[i % 2] * B
    line_neg += c[(i + 1) % 2] * B
for i in range(N):
    if i % 2 == 0:
        for _ in range(A):
            print(line_pos)
    else:
        for _ in range(A):
            print(line_neg)
