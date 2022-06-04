from bisect import bisect, bisect_left


def solve(N):
    A = [i**2 for i in range(1, N + 1)]
    seen = set(A)
    ret = 0

    for i in range(1, N + 1):
        if i not in seen:
            j = bisect(A, N / i)
        else:
            j = bisect(A, N) - bisect_left(A, i)
        ret += j * 2 - 1
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
        print(i, r)
    return ret


def main():
    N = int(input())
    ret = naive(N)
    print(ret)


main()


# for i in range(1, 101):
#     sol = solve(i)
#     nai = naive(i)
#     if sol != nai:
#         print(i, sol, nai)
