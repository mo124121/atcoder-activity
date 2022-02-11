#!/usr/bin/env python3
import sys


def solve(K: int):
    sqrt_K = int(K ** 0.5)
    deviders = {}
    for i in range(1, sqrt_K + 1):
        if K % i == 0:
            deviders[i] = True
            deviders[K // i] = True
    deviders = list(deviders.keys())
    deviders.sort()
    # print(deviders)
    ret = 0
    for i in range(len(deviders)):
        for j in range(i, len(deviders)):
            if K / deviders[i] < deviders[j]:  # 大きすぎるa x bの除去
                continue
            if K % (deviders[i] * deviders[j]) != 0:
                continue
            if deviders[j] <= K / (deviders[i] * deviders[j]):
                ret += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)


if __name__ == "__main__":
    main()
