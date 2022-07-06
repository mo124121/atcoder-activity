A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

FILLED = -1


def fill(b):
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                A[i][j] = FILLED
                return
    return


def check():
    flag = False
    # tate
    for i in range(3):
        c = 0
        for j in range(3):
            if A[i][j] == FILLED:
                c += 1
        if c == 3:
            flag = True
            break
    # yoko
    for i in range(3):
        c = 0
        for j in range(3):
            if A[j][i] == FILLED:
                c += 1
        if c == 3:
            flag = True
            break
    # naname
    c = 0
    for i in range(3):
        if A[i][i] == FILLED:
            c += 1
    if c == 3:
        flag = True
    c = 0
    for i in range(3):
        if A[i][2 - i] == FILLED:
            c += 1
    if c == 3:
        flag = True

    return flag


for b in B:
    fill(b)

if check():
    print("Yes")
else:
    print("No")
