from itertools import product


def naive(n, k):
    cakes = []
    for pat in product(list(range(1, n + 1)), repeat=3):
        cakes.append((sum(pat), pat[0], pat[2], pat))
    cakes.sort()
    return cakes[k - 1][3]


def solve(N, K):
    cum = 0
    for z in range(3, 3 + N + 1):
        cz = (
            (
                min(N, z - 2)
                - max(
                    1,
                )
            )
            * (z - 1)
            // 2
        )
        if cum + cz >= K:
            break
        cum += cz

    K -= cum
    cum = 0
    for a in range(max(1, z - 2 * N), min(N, z - 2) + 1):
        ca = z - a
        if cum + ca >= K:
            break
        cum += ca
    b = K - cum
    c = z - a - b
    return a, b, c


def main():
    N, K = map(int, input().split())
    print(*solve(N, K))


main()
