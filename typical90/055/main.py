#!/usr/bin/env python3
import sys

MOD = 7  # type: int


def solve(N: int, P: int, Q: int, A: "List[int]"):
    ret=0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                for l in range(k+1,N):
                    for m in range(l+1,N):
                        prod = A[i]*A[j]%P*A[k]%P*A[l]%P*A[m]%P
                        if prod==Q:
                            ret+=1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, Q, A)

if __name__ == '__main__':
    main()
