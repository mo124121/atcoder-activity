A, B, K = map(int, input().split())

for i in range(100):
    if A >= B:
        print(i)
        exit()
    A *= K
