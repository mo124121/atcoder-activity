N = int(input())
S = [input() for _ in range(N)]

MOVES = [(1, 0), (0, 1), (1, 1), (-1, 1)]

for i in range(N):
    for j in range(N):
        for mv in MOVES:
            count = 0
            flag = True
            for k in range(6):
                x = i + mv[0] * k
                y = j + mv[1] * k
                if x < 0 or x > N - 1 or y < 0 or y > N - 1:
                    flag = False
                    break
                if S[x][y] == "#":
                    count += 1
            if flag and count >= 4:
                print("Yes")
                exit()

print("No")
