N = int(input())
S = input()

T = "b"
M = N // 2
for i in range(1, M + 1):
    if i % 3 == 1:
        T = "a" + T + "c"
    elif i % 3 == 2:
        T = "c" + T + "a"
    else:
        T = "b" + T + "b"

if S == T:
    print(M)
else:
    print(-1)
