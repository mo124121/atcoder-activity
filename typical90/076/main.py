#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, A: "List[int]"):
    right = 0
    total_sum = sum(A)
    partial_sum = A[0]
    for left in range(N):
        while True:
            if partial_sum * 10 == total_sum:
                print(YES)
                return
            elif partial_sum * 10 < total_sum:
                right = (right + 1) % N
                partial_sum += A[right]
            else:
                break
        if right == left:
            right = (right + 1) % N
            partial_sum += A[right]
        partial_sum -= A[left]
    print(NO)

    return


N = int(input())
A = list(map(int, input().split()))
solve(N, A)
