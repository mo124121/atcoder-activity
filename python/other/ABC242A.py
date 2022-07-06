A, B, C, X = map(int, input().split())

if X <= A:
    print(1)
elif X <= B:
    print("{:.7f}".format(C / (B - A)))
else:
    print(0)
