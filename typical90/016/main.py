#!/usr/bin/env python3
import sys


def solve(N: int, A: int, B: int, C: int):
    MAX_NUM = max(N // A, N // B, N // C)
    ret = MAX_NUM
    for i in range(MAX_NUM + 1 - 2):
        for j in range(MAX_NUM + 1 - 1 - i):
            target = N - i * A - j * B
            if target >= 0 and target % C == 0:
                ret = min(ret, i + j + target // C)
    print(ret)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(N, A, B, C)


if __name__ == "__main__":
    main()
