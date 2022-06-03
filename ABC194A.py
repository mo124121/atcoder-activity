def solve(A, B):
    C = A + B
    if C >= 15 and B >= 8:
        return 1
    elif C >= 10 and B >= 3:
        return 2
    elif C >= 3:
        return 3
    else:
        return 4


def main():
    A, B = map(int, input().split())
    r = solve(A, B)
    print(r)


main()
