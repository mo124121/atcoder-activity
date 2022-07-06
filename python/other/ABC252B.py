N, K = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split()))

C = [(A[i], i + 1) for i in range(N)]
C.sort(reverse=True)
a = C[0][0]
for x, i in C:
    if x != a:
        print("No")
        exit()
    if i in B:
        print("Yes")
        exit()
print("No")
