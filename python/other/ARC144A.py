N = int(input())

print(2 * N)
x = "4" * (N // 4)
if N % 4 != 0:
    x = str(N % 4) + x
print(x)
