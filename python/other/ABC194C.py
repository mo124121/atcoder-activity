N = int(input())
A = list(map(int, input().split()))

ret = 0

aj = sum(A)
aj2 = sum([a**2 for a in A])

for i, a in enumerate(A[:-1]):
    aj -= a
    aj2 -= a**2
    ret += a**2 * (N - i - 1)
    ret -= 2 * a * aj
    ret += aj2


print(ret)
