A, B, C = map(int, input().split())

dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]


def rec(a, b, c):
    if dp[a][b][c]:
        return dp[a][b][c]
    if a == 100 or b == 100 or c == 100:
        return 0
    ret = 0
    ret += (rec(a + 1, b, c) + 1) * a / (a + b + c)
    ret += (rec(a, b + 1, c) + 1) * b / (a + b + c)
    ret += (rec(a, b, c + 1) + 1) * c / (a + b + c)
    dp[a][b][c] = ret
    return ret


print("{:.9f}".format(rec(A, B, C)))

"""
愚直なら3^(3N-A-B-C)　んなこたあない

dpっぽい

解説後
漸化式を書くべき
遷移前・遷移後で期待値の関係性が存在するはず
"""
