N, A, B = map(int, input().split())

if N > 5:
    print(B * 5 + (N - 5) * A)
else:
    print(B * N)
