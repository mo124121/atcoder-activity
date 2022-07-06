n = int(input())

c = ((n - 1) // 20) % 2

if c == 0:
    print((n - 1) % 20 + 1)
else:
    print(20 - (n - 1) % 20)
