N, M, K, S, T, X = map(int, input().split())

MOD = 998244353
edge = []
for i in range(M):
    u, v = map(int, input().split())
    edge.append((u, v))
    edge.append((v, u))

dp = [[[0] * (N + 1) for _ in range(K + 1)] for _ in range(2)]
dp[0][0][S] = 1
for i in range(K):
    for u, v in edge:
        for x in [0, 1]:
            dp[x][i + 1][u] += dp[x ^ (v == X)][i][v]
            dp[x][i + 1][u] %= MOD

print(dp[0][K][T])


"""
dpっぽい
dp[i][k]:頂点iにおけるk個使った時の通り数

発想を変える
パス×寄り道のパターン数


XOR 
  1 0
1 0 1
0 1 0
"""

# stack = []
# stack.append((0, S))
# ret = 0
# while len(stack) > 0:
#     k, node = stack.pop()

#     if k == K:
#         if node == T:
#             ret += 1
#         continue
#     for neibor in G[node]:
#         stack.append((k + 1, neibor))


# print(ret)
"""
  1
 / \
2   4
 \ /
  3

K=2000
N=2000
1
2 3 4 5 6 ~ 2000

1999*1*1999*1*1999~~~~1*1999
1999^(2000//2)=1999^1000

"""
