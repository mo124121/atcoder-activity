from math import log2


n = int(input())


if n > 2 * log2(n):
    print("Yes")
else:
    print("No")
