X, A, D, N = map(int, input().split())

if D == 0:
    print(abs(X - A))
    exit()
B = A + (N - 1) * D
if A > B:
    A, B = B, A
    D *= -1


l = 1
r = N
while r - l > 1:
    m = (r + l) // 2
    Y = A + (m - 1) * D
    if X < Y:
        r = m
    else:
        l = m
L = A + (l - 1) * D
R = A + (r - 1) * D
print(min(abs(L - X), abs(R - X)))
