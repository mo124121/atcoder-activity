N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_pre = A[0]
b_pre = B[0]

for i in range(1, N):
    a = A[i]
    b = B[i]
    a_next = -1
    b_next = -1
    if a_pre != -1:
        if abs(a - a_pre) <= K:
            a_next = a
        if abs(b - a_pre) <= K:
            b_next = b
    if b_pre != -1:
        if abs(a - b_pre) <= K:
            a_next = a
        if abs(b - b_pre) <= K:
            b_next = b
    a_pre, b_pre = a_next, b_next
    if a_pre == -1 and b_pre == -1:
        print("No")
        exit()
print("Yes")
