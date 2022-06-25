N, X = map(int, input().split())

for i in range(26):
    if X <= N:
        print(chr(ord("A") + i))
        exit()
    X -= N
