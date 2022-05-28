def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def mcm(x, y):
    return x // gcd(x, y) * y


def solve(N, A, B):

    N_sum = N * (N + 1) // 2
    a = N // A
    a_sum = A * a * (a + 1) // 2
    b = N // B
    b_sum = B * b * (b + 1) // 2
    AB = mcm(A, B)
    ab = N // (AB)
    ab_sum = AB * ab * (ab + 1) // 2
    return N_sum - (a_sum + b_sum - ab_sum)


def naive(N, A, B):
    ret = 0
    for i in range(1, N + 1):
        if i % A != 0 and i % B != 0:
            ret += i
    return ret


N, A, B = map(int, input().split())
ret = solve(N, A, B)
print(ret)
size = 100
n = 100
for a in range(1, size):
    for b in range(1, size):
        sol = solve(n, a, b)
        nai = naive(n, a, b)
        if sol != nai:
            print(n, a, b, sol, nai)

# solve(2, 2, 2)
