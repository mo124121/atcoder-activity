import sys
from collections import defaultdict, deque


def solve(N: int, A: "List[int]", B: "List[int]"):

    G = defaultdict(list)
    for i in range(N - 1):
        G[A[i]].append(B[i])
        G[B[i]].append(A[i])

    ret = [[] for _ in range(2)]

    st = deque()
    st.append(1)
    seen = {1: 0}

    while len(st):
        node = st.pop()
        for neibor in G[node]:
            if neibor not in seen:
                st.append(neibor)
                seen[neibor] = 1 - seen[node]
                ret[seen[neibor]].append(neibor)

    if len(ret[0]) > len(ret[1]):
        print(*ret[0][: N // 2])
    else:
        print(*ret[1][: N // 2])

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)


if __name__ == "__main__":
    main()
