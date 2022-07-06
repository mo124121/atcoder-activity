a, b = list(map(int, input().split()))
Y = "Yes"
N = "No"
if abs(a - b) in [1, 9]:
    print(Y)
else:
    print(N)
