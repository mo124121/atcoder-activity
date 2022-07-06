X = int(input())

c = X // 100
v = X % 100
if c >= (v + 5 - 1) // 5:
    print(1)
else:
    print(0)
