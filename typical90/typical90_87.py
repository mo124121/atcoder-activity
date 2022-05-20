N, P, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
INF = 10**18


def wf(x):
    dp = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a = A[i][j]
            if a == -1:
                dp[i][j] = x
            else:
                dp[i][j] = A[i][j]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    ret = 0

    for i in range(N - 1):
        for j in range(i + 1, N):
            if dp[i][j] <= P:
                ret += 1
    return ret


def bs(K):
    l = 0
    r = INF
    while l + 1 < r:
        m = (r + l) // 2
        if wf(m) >= K:
            l = m
        else:
            r = m
    return l


left = bs(K)
right = bs(K + 1)
if left == INF - 1:
    if right == INF - 1:
        print(0)
    else:
        print("Infinity")
else:
    print(left - right)


"""
WFの記憶が曖昧
二分探索の境界が微妙
二分探索の対象を1つずらして数をカウントする
端っこになる場合の挙動を考える
"""
