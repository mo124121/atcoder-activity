def solve(H, N, A, B):
    INF = 10**18
    dp = [INF] * (H + 1)
    dp[0] = 0
    for i in range(N):
        a, b = A[i], B[i]
        for h in range(H):
            nxt = min(H, h + a)
            dp[nxt] = min(dp[h] + b, dp[nxt])
    return dp[H]


def submit():
    H, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = solve(H, N, A, B)
    print(ans)


submit()
test = [
    [9, 3, [8, 4, 2], [3, 2, 1]],
    # [10**4, 10**3, [1] * (10**3), [i for i in range(10**3, 0, -1)]],
    [
        10**4,
        10**3,
        [i for i in range(10**3, 0, -1)],
        [i * 2 for i in range(10**3, 0, -1)],
    ],
    [1, 1, [1], [1]],
    [10**4, 10**3, [1] * (10**3), [10**4] * (10**3)],
]
for t in test:
    print(solve(*t))
"""
これは貪欲かと思ったらDPで解かなきゃいけないパターンに見える
というかこれ個数制限なしナップサック問題では
1WAがとれん


"""
