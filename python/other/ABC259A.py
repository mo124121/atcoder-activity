N, M, X, T, D = map(int, input().split())

if M >= X:
    print(T)
else:
    init = T - X * D
    print(init + D * M)
