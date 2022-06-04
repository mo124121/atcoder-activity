from bisect import bisect, bisect_left


def solve(N):
    ret = 0

    for i in range(1, N + 1):
        k = i
        j = 2
        while j**2 <= k:
            while k % j**2 == 0:
                k //= j**2
            j += 1

        j = 1
        while k * j**2 <= N:
            ret += 1
            j += 1
    return ret


def naive(N):
    ret = 0
    for i in range(1, N + 1):
        r = 0
        for j in range(1, N + 1):
            e = (i * j) ** 0.5
            if abs(e - int(e)) < 0.0000001:
                r += 1
        ret += r
    return ret


def main():
    N = int(input())
    ret = solve(N)
    print(ret)


main()


# for i in range(1, 101):
#     sol = solve(i)
#     nai = naive(i)
#     if sol != nai:
#         print(i, sol, nai)


# for i in range(1, 101):
#     print(i, naive(i))
