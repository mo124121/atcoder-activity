#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, S: str):
    ATCODER = " atcoder"
    S = " " + S
    dp = [[0] * len(S) for _ in range(len(ATCODER))]
    for j in range(len(S)):
        dp[0][j] = 1
    prev_start = 0
    for i in range(1, len(ATCODER)):
        for j in range(prev_start + 1, len(S)):
            dp[i][j] += dp[i][j - 1]
            if S[j] == ATCODER[i]:
                dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] %= MOD
        for j in range(prev_start, len(S)):
            if dp[i][j] != 0:
                prev_start = j
                break
    print(dp[len(ATCODER) - 1][len(S) - 1])
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == "__main__":
    main()
