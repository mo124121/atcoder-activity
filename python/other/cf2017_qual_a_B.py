N, M, K = map(int, input().split())

for i in range(N + 1):
    for j in range(M + 1):
        if K == i * M + j * (N - i - i):
            print("Yes")
            exit()
print("No")


"""
先に行ボタンを押してKを超えるまで操作した後で、
列ボタンで減らせるときに到達できるか？的な？
証明はできない

N,M<1000
N*Mでまにあう　ごり押しするか



"""
