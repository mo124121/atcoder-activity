#!/usr/bin/env python3
import bisect


def solve(N: int, A: "List[int]", Q: int, B: "List[int]"):
    A.sort()
    A = [-(10 ** 9) - 1] + A
    A.append(2 * 10 ** 9 + 1)
    for b in B:
        i = bisect.bisect(A, b)
        ret = min(b - A[i - 1], A[i] - b)
        print(ret)
    return


def main():

    N = int(input())  # type: int
    A = list(map(int, input().split()))
    Q = int(input())  # type: int
    B = [int(input()) for _ in range(Q)]  # type: "List[int]"
    solve(N, A, Q, B)


if __name__ == "__main__":
    main()
