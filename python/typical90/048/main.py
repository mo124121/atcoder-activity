#!/usr/bin/env python3
import sys
import heapq


def solve(N: int, K: int, A: "List[int]", B: "List[int]"):
    AB = [[B[i], A[i]] for i in range(N)]
    AB.sort(reverse=True)
    B = [AB[i][0] for i in range(N)]
    A = [AB[i][1] - AB[i][0] for i in range(N)]
    A_heap = []
    t = 0
    ret = 0
    i = 0
    while K > t:
        t += 1
        if i < N:
            if len(A_heap) == 0:
                ret += B[i]
                heapq.heappush(A_heap, -A[i])
                i += 1
            else:
                a_current = -heapq.heappop(A_heap)
                if a_current < B[i]:
                    heapq.heappush(A_heap, -a_current)
                    ret += B[i]
                    heapq.heappush(A_heap, -A[i])
                    i += 1
                else:
                    ret += a_current
        else:
            if len(A_heap):
                ret += -heapq.heappop(A_heap)
            else:
                t = 2 * N
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
    K = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, K, A, B)


if __name__ == "__main__":
    main()