N = int(input())
a = 1

while 3**a <= N:
    b = 1
    while 3**a + 5**b <= N:
        if 3**a + 5**b == N:
            print(a, b)
            exit()
        b += 1
    a += 1
print(-1)
