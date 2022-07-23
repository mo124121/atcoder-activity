N = int(input())
A = [input() for _ in range(N)]


def no():
    print("incorrect")
    exit()


for i in range(2, N):
    for j in range(i):
        if A[i][j] == "W" and A[j][i] != "L":
            no()
        if A[i][j] == "L" and A[j][i] != "W":
            no()
        if A[i][j] == "D" and A[j][i] != "D":
            no()


print("correct")
