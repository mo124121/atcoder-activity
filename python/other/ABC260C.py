N, X, Y = map(int, input().split())


def red(n):
    if n == 1:
        return 0
    return red(n - 1) + blue(n) * X


def blue(n):
    if n == 1:
        return 1
    return red(n - 1) + blue(n - 1) * Y


print(red(N))
