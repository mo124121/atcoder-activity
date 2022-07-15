N, M, A, B = map(int, input().split())

for i in range(1, M + 1):
    c = int(input())
    if N <= A:
        N += B
    N -= c
    if N < 0:
        print(i)
        exit()
print("complete")
